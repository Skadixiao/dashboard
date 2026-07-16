import re

import requests


URL = "https://investor.sandisk.com/news-events/events"
MIRROR_URL = "https://r.jina.ai/http://https://investor.sandisk.com/news-events/events"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}


def clean_text(text):
    return " ".join(text.split()) if text else ""


def _extract_from_markdown(markdown_text):
    section_match = re.search(
        r"(?is)^##\s+Upcoming Events\s*(.*?)(?:^##\s+Past Events|\Z)",
        markdown_text,
        re.MULTILINE,
    )

    if not section_match:
        return []

    section = section_match.group(1)
    date_pattern = re.compile(
        r"^(?P<datetime>[A-Z][a-z]{2,8} \d{1,2}, \d{4} \d{1,2}:\d{2} (?:AM|PM) [A-Z]{3})$",
        re.MULTILINE,
    )

    events = []
    for match in date_pattern.finditer(section):
        event_datetime = clean_text(match.group("datetime"))
        if not event_datetime:
            continue

        events.append(
            {
                "section": "Upcoming Events",
                "title": f"SanDisk event ({event_datetime})",
                "url": URL,
                "datetime": event_datetime,
            }
        )

    return events


def scrape_sandisk_upcoming_events():
    try:
        response = requests.get(URL, timeout=15, headers=HEADERS)
        response.raise_for_status()
    except Exception:
        pass
    else:
        # The site is occasionally slow to render in this environment, so
        # we only keep the direct HTML path when the request actually returns.
        return _extract_from_markdown(response.text)

    mirror_response = requests.get(MIRROR_URL, timeout=30, headers=HEADERS)
    mirror_response.raise_for_status()
    return _extract_from_markdown(mirror_response.text)

