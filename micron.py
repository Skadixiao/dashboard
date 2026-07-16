import re
import ssl
from html import unescape
from urllib.request import Request, urlopen
from urllib.parse import urljoin


URL = "https://investors.micron.com/events-and-presentations"


def clean_text(text: str) -> str:
    """Remove unnecessary spaces and line breaks from extracted HTML text."""
    return " ".join(text.split()) if text else ""


def extract_micron_upcoming_events() -> list[dict]:
    """Fetch Micron's upcoming investor events from the official events page."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0.0.0 Safari/537.36"
        )
    }

    request = Request(URL, headers=headers)
    context = ssl._create_unverified_context()

    with urlopen(request, context=context, timeout=60) as response:
        html = response.read().decode("utf-8", errors="ignore")

    upcoming_table_match = re.search(
        r'(?is)<div class="nir-widget--label">\s*Upcoming Events\s*</div>.*?'
        r'<table class="nirtable collapse-table upcoming-events">(.*?)</table>',
        html,
    )

    if not upcoming_table_match:
        raise ValueError("Upcoming Events table not found on Micron page.")

    table_html = upcoming_table_match.group(1)
    rows = re.findall(r"(?is)<tr>(.*?)</tr>", table_html)
    events = []

    for row in rows:
        if "<th>" in row:
            continue

        date_match = re.search(
            r'(?is)<div class="nir-widget--field nir-widget--event--date">(.*?)</div>',
            row,
        )
        title_match = re.search(
            r'(?is)<div class="nir-widget--field nir-widgets--event--title">(.*?)</div>',
            row,
        )

        if not date_match or not title_match:
            continue

        date_cell = clean_text(re.sub(r"<.*?>", " ", date_match.group(1)))
        title_cell = title_match.group(1)
        title_link_match = re.search(
            r'(?is)<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
            title_cell,
        )

        if not title_link_match:
            continue

        href = title_link_match.group(1)
        title = clean_text(unescape(re.sub(r"<.*?>", " ", title_link_match.group(2))))

        events.append(
            {
                "section": "Upcoming Events",
                "datetime": date_cell,
                "title": title,
                "url": urljoin(URL, href),
            }
        )

    return events
