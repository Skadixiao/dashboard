import re
from datetime import datetime, timezone

import pandas as pd
import streamlit as st
from dateutil import parser

from microsoft import extract_upcoming_event
from micron import extract_micron_upcoming_events
from sandisk import scrape_sandisk_upcoming_events


TIMEZONE_ABBREVIATIONS = {
    "PT": -7 * 3600,
    "PDT": -7 * 3600,
    "MT": -6 * 3600,
    "MDT": -6 * 3600,
    "CT": -5 * 3600,
    "CDT": -5 * 3600,
    "ET": -4 * 3600,
    "EDT": -4 * 3600,
    "EST": -4 * 3600,
}


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Investor Event Calendar",
    page_icon="📅",
    layout="wide",
)


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def normalise_event(company, event):
    """
    Convert an event from an individual scraper into a standard format.

    Expected event fields:
        datetime
        title
        url, optional
    """

    return {
        "company": company,
        "datetime": parse_event_datetime(event.get("datetime")),
        "title": event.get("title", "Untitled event"),
        "url": event.get("url", ""),
    }


def parse_event_datetime(value):
    """
    Convert raw scraper date strings into a timezone-aware UTC timestamp.
    """

    if value is None:
        return pd.NaT

    if isinstance(value, pd.Timestamp):
        if value.tzinfo is None:
            return value.tz_localize("UTC")
        return value.tz_convert("UTC")

    if isinstance(value, datetime):
        if value.tzinfo is None:
            return pd.Timestamp(value).tz_localize("UTC")
        return pd.Timestamp(value).tz_convert("UTC")

    if not isinstance(value, str):
        return pd.NaT

    cleaned = re.sub(r"\s+", " ", value.strip())
    cleaned = cleaned.replace(" at ", " ").replace(" - ", " ")

    try:
        parsed = parser.parse(cleaned, tzinfos=TIMEZONE_ABBREVIATIONS)
    except Exception:
        return pd.NaT

    if parsed.tzinfo is None:
        return pd.Timestamp(parsed).tz_localize("UTC")

    return pd.Timestamp(parsed).tz_convert("UTC")


@st.cache_data(ttl=1800, show_spinner=False)
def load_events():
    """
    Run all company scrapers and combine their outputs.

    Cache results for 30 minutes so Streamlit does not repeatedly
    scrape every website whenever the user clicks a filter.
    """

    all_events = []
    errors = []

    # Microsoft currently returns one dictionary
    try:
        microsoft_event = extract_upcoming_event()

        if microsoft_event:
            all_events.append(
                normalise_event("Microsoft", microsoft_event)
            )

    except Exception as exc:
        errors.append(f"Microsoft: {exc}")

    # Micron returns a list of dictionaries
    try:
        micron_events = extract_micron_upcoming_events() or []

        for event in micron_events:
            all_events.append(
                normalise_event("Micron", event)
            )

    except Exception as exc:
        errors.append(f"Micron: {exc}")

    # SanDisk returns a list of dictionaries
    try:
        sandisk_events = scrape_sandisk_upcoming_events() or []

        for event in sandisk_events:
            all_events.append(
                normalise_event("SanDisk", event)
            )

    except Exception as exc:
        errors.append(f"SanDisk: {exc}")

    dataframe = pd.DataFrame(all_events)

    if dataframe.empty:
        dataframe = pd.DataFrame(
            columns=["company", "datetime", "title", "url"]
        )
        return dataframe, errors

    dataframe["datetime"] = dataframe["datetime"].apply(
        parse_event_datetime
    )
    dataframe = dataframe.dropna(subset=["datetime"]).copy()
    dataframe = dataframe.sort_values("datetime").reset_index(drop=True)

    return dataframe, errors


def format_countdown(event_datetime):
    """
    Create a human-readable countdown.
    """

    now = pd.Timestamp.now(tz="UTC")
    difference = event_datetime - now

    total_seconds = int(difference.total_seconds())

    if total_seconds < 0:
        return "Event has started or passed"

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60

    if days > 0:
        return f"In {days} days and {hours} hours"

    if hours > 0:
        return f"In {hours} hours and {minutes} minutes"

    return f"In {minutes} minutes"


# ---------------------------------------------------------
# Load data
# ---------------------------------------------------------

st.title("Investor Event Calendar")

st.caption(
    "Upcoming official investor events for companies on my watchlist."
)

with st.spinner("Collecting upcoming events..."):
    events_df, scraper_errors = load_events()


# ---------------------------------------------------------
# Sidebar controls
# ---------------------------------------------------------

st.sidebar.header("Filters")

if st.sidebar.button("Refresh event data"):
    st.cache_data.clear()
    st.rerun()


available_companies = sorted(events_df["company"].unique().tolist())

selected_companies = st.sidebar.multiselect(
    "Companies",
    options=available_companies,
    default=available_companies,
)

time_period = st.sidebar.selectbox(
    "Show events within",
    options=[
        "All upcoming events",
        "Next 7 days",
        "Next 30 days",
        "Next 90 days",
        "Next 365 days",
    ],
)


# ---------------------------------------------------------
# Filter events
# ---------------------------------------------------------

now = pd.Timestamp.now(tz="UTC")

filtered_df = events_df[
    events_df["company"].isin(selected_companies)
].copy()

# Only show current and future events
filtered_df = filtered_df[
    filtered_df["datetime"] >= now
]

period_days = {
    "Next 7 days": 7,
    "Next 30 days": 30,
    "Next 90 days": 90,
    "Next 365 days": 365,
}

if time_period in period_days:
    maximum_date = now + pd.Timedelta(days=period_days[time_period])

    filtered_df = filtered_df[
        filtered_df["datetime"] <= maximum_date
    ]


# ---------------------------------------------------------
# Scraper error reporting
# ---------------------------------------------------------

if scraper_errors:
    with st.expander("Some websites could not be updated"):
        for error in scraper_errors:
            st.warning(error)


# ---------------------------------------------------------
# Dashboard metrics
# ---------------------------------------------------------

metric_col1, metric_col2, metric_col3 = st.columns(3)

metric_col1.metric(
    "Upcoming events",
    len(filtered_df),
)

metric_col2.metric(
    "Companies tracked",
    events_df["company"].nunique(),
)

if not filtered_df.empty:
    next_event = filtered_df.iloc[0]

    metric_col3.metric(
        "Next event",
        next_event["company"],
    )
else:
    metric_col3.metric(
        "Next event",
        "None found",
    )


# ---------------------------------------------------------
# Next event section
# ---------------------------------------------------------

st.divider()
st.subheader("Next Important Event")

if filtered_df.empty:
    st.info("No upcoming events were found for the selected filters.")

else:
    next_event = filtered_df.iloc[0]

    next_event_datetime_uk = next_event["datetime"].tz_convert(
        "Europe/London"
    )

    st.markdown(
        f"""
        ### {next_event['company']}

        **{next_event['title']}**

        {next_event_datetime_uk.strftime("%A, %d %B %Y at %H:%M")} UK time

        **{format_countdown(next_event['datetime'])}**
        """
    )

    if next_event["url"]:
        st.link_button(
            "View official event page",
            next_event["url"],
        )


# ---------------------------------------------------------
# Event cards
# ---------------------------------------------------------

st.divider()
st.subheader("Upcoming Events")

if not filtered_df.empty:

    # Three cards per row
    for start_index in range(0, len(filtered_df), 3):

        columns = st.columns(3)

        row_events = filtered_df.iloc[start_index:start_index + 3]

        for column, (_, event) in zip(columns, row_events.iterrows()):

            event_datetime_uk = event["datetime"].tz_convert(
                "Europe/London"
            )

            with column:
                with st.container(border=True):

                    st.caption(event["company"])

                    st.markdown(
                        f"#### {event['title']}"
                    )

                    st.write(
                        event_datetime_uk.strftime(
                            "%A, %d %B %Y"
                        )
                    )

                    st.write(
                        event_datetime_uk.strftime(
                            "%H:%M UK time"
                        )
                    )

                    st.caption(
                        format_countdown(event["datetime"])
                    )

                    if event["url"]:
                        st.link_button(
                            "Official page",
                            event["url"],
                            use_container_width=True,
                        )


# ---------------------------------------------------------
# Table view
# ---------------------------------------------------------

st.divider()
st.subheader("All Event Details")

if not filtered_df.empty:

    table_df = filtered_df.copy()

    table_df["UK date"] = (
        table_df["datetime"]
        .dt.tz_convert("Europe/London")
        .dt.strftime("%d %b %Y")
    )

    table_df["UK time"] = (
        table_df["datetime"]
        .dt.tz_convert("Europe/London")
        .dt.strftime("%H:%M")
    )

    table_df["Countdown"] = table_df["datetime"].apply(
        format_countdown
    )

    table_df = table_df[
        [
            "company",
            "title",
            "UK date",
            "UK time",
            "Countdown",
            "url",
        ]
    ]

    table_df = table_df.rename(
        columns={
            "company": "Company",
            "title": "Event",
            "url": "Official link",
        }
    )

    st.dataframe(
        table_df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Official link": st.column_config.LinkColumn(
                "Official link",
                display_text="Open",
            )
        },
    )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "Event information is collected from official company investor "
    "relations websites. Always confirm the time on the official page."
)