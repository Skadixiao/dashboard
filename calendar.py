import csv
import json
import re
from datetime import datetime, timezone
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from dateutil import parser as date_parser


BASE_URL = "https://www.microsoft.com"
EVENTS_URL = "https://www.microsoft.com/en-us/investor/events/default"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
    )
}


def get_page(url):
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )
    response.raise_for_status()

    return response.text


def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()


def classify_event(title):
    title_lower = title.lower()

    if "earnings" in title_lower:
        return "Earnings"

    if "quarter" in title_lower:
        return "Earnings"

    if "annual meeting" in title_lower:
        return "Shareholder Meeting"

    if "shareholder" in title_lower:
        return "Shareholder Meeting"

    if "conference" in title_lower:
        return "Conference"

    if "investor" in title_lower:
        return "Investor Event"

    if "analyst" in title_lower:
        return "Investor Event"

    return "Other"


def extract_date(text):
    months = (
        "January|February|March|April|May|June|"
        "July|August|September|October|November|December"
    )

    date_pattern = re.compile(
        rf"\b(?:{months})\s+\d{{1,2}},\s+\d{{4}}\b",
        re.IGNORECASE
    )

    match = date_pattern.search(text)

    if match:
        return match.group(0)

    return None


def extract_time(text):
    time_pattern = re.compile(
        r"\b\d{1,2}:\d{2}\s*(?:AM|PM)\b"
        r"(?:\s*-\s*(?:PT|PST|PDT|ET|EST|EDT|UTC|GMT))?",
        re.IGNORECASE
    )

    match = time_pattern.search(text)

    if match:
        return match.group(0)

    return None


def extract_timezone(text):
    timezone_pattern = re.compile(
        r"\b(PT|PST|PDT|ET|EST|EDT|UTC|GMT)\b",
        re.IGNORECASE
    )

    match = timezone_pattern.search(text)

    if match:
        return match.group(1).upper()

    return None


def parse_event_date(date_text):
    if not date_text:
        return None

    try:
        parsed_date = date_parser.parse(date_text)

        return parsed_date.strftime("%Y-%m-%d")

    except ValueError:
        return None


def find_event_container(link):
    current_element = link

    for _ in range(7):
        parent = current_element.parent

        if parent is None:
            break

        parent_text = clean_text(
            parent.get_text(
                " ",
                strip=True
            )
        )

        if extract_date(parent_text):
            return parent

        current_element = parent

    return link.parent


def scrape_microsoft_events():
    html = get_page(EVENTS_URL)

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    events = []
    seen_urls = set()

    links = soup.find_all(
        "a",
        href=True
    )

    for link in links:
        href = link.get("href", "")

        if "/en-us/investor/events/" not in href:
            continue

        event_url = urljoin(
            BASE_URL,
            href
        )

        if event_url.rstrip("/") == EVENTS_URL.rstrip("/"):
            continue

        if event_url in seen_urls:
            continue

        title = clean_text(
            link.get_text(
                " ",
                strip=True
            )
        )

        if not title:
            continue

        if len(title) < 5:
            continue

        container = find_event_container(link)

        if container is None:
            container_text = title

        else:
            container_text = clean_text(
                container.get_text(
                    " ",
                    strip=True
                )
            )

        raw_date = extract_date(container_text)
        raw_time = extract_time(container_text)
        timezone_name = extract_timezone(
            raw_time or container_text
        )

        event = {
            "company": "Microsoft Corporation",
            "ticker": "MSFT",
            "event_title": title,
            "event_type": classify_event(title),
            "event_date": parse_event_date(raw_date),
            "raw_date": raw_date,
            "event_time": raw_time,
            "timezone": timezone_name,
            "source_url": event_url,
            "source_page": EVENTS_URL,
            "scraped_at_utc": datetime.now(
                timezone.utc
            ).isoformat()
        }

        events.append(event)
        seen_urls.add(event_url)

    return events


def sort_events(events):
    def sort_key(event):
        event_date = event.get("event_date")

        if not event_date:
            return datetime.max

        try:
            return datetime.strptime(
                event_date,
                "%Y-%m-%d"
            )

        except ValueError:
            return datetime.max

    return sorted(
        events,
        key=sort_key
    )


def save_to_csv(events, filename):
    if not events:
        return

    fieldnames = [
        "company",
        "ticker",
        "event_title",
        "event_type",
        "event_date",
        "raw_date",
        "event_time",
        "timezone",
        "source_url",
        "source_page",
        "scraped_at_utc"
    ]

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(events)


def save_to_json(events, filename):
    result = {
        "company": "Microsoft Corporation",
        "ticker": "MSFT",
        "generated_at_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "event_count": len(events),
        "events": events
    }

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            ensure_ascii=False,
            indent=2
        )


def print_events(events):
    print()
    print("=" * 80)
    print("Microsoft Investor Relations Calendar")
    print("=" * 80)

    if not events:
        print("No events found.")
        return

    for event in events:
        print()
        print(
            f"Date: {event['event_date'] or event['raw_date'] or 'Unknown'}"
        )

        print(
            f"Time: {event['event_time'] or 'Unknown'}"
        )

        print(
            f"Type: {event['event_type']}"
        )

        print(
            f"Title: {event['event_title']}"
        )

        print(
            f"URL: {event['source_url']}"
        )

        print("-" * 80)


def main():
    try:
        events = scrape_microsoft_events()

        events = sort_events(events)

        print_events(events)

        save_to_csv(
            events,
            "microsoft_ir_calendar.csv"
        )

        save_to_json(
            events,
            "microsoft_ir_calendar.json"
        )

        print()
        print(
            f"Successfully collected {len(events)} events."
        )

        print(
            "Saved to microsoft_ir_calendar.csv"
        )

        print(
            "Saved to microsoft_ir_calendar.json"
        )

    except requests.RequestException as error:
        print(
            f"Request failed: {error}"
        )

    except Exception as error:
        print(
            f"Unexpected error: {error}"
        )


if __name__ == "__main__":
    main()