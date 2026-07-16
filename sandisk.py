from urllib.parse import urljoin

from playwright.sync_api import sync_playwright


URL = "https://investor.sandisk.com/news-events/events"


def clean_text(text):
    return " ".join(text.split()) if text else ""


def scrape_sandisk_upcoming_events():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-http2"],
        )

        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        )

        page.set_default_timeout(60_000)

        page.goto(URL, wait_until="commit", timeout=60_000)

        heading = page.locator("h2", has_text="Upcoming Events").first
        heading.wait_for(state="visible", timeout=60_000)

        upcoming_content = heading.locator(
            "xpath=following-sibling::div"
            "[contains(@class, 'nir-widget--content')][1]"
        )

        articles = upcoming_content.locator("article")
        events = []

        for index in range(articles.count()):
            article = articles.nth(index)

            title_link = article.locator(".nir-widgets--event--title a").first
            if title_link.count() == 0:
                continue

            title = clean_text(title_link.inner_text())
            href = title_link.get_attribute("href") or ""

            date_element = article.locator(".nir-widget--event--date").first
            event_datetime = ""
            if date_element.count() > 0:
                event_datetime = clean_text(date_element.inner_text())

            events.append(
                {
                    "section": "Upcoming Events",
                    "title": title,
                    "url": urljoin(URL, href),
                    "datetime": event_datetime,
                }
            )

        browser.close()
        return events


