from playwright.sync_api import sync_playwright


URL = "https://www.microsoft.com/en-us/investor/events/default"


def clean_text(text: str) -> str:
    """Remove unnecessary spaces and line breaks."""
    return " ".join(text.split())


def extract_upcoming_event() -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            locale="en-US",
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
        )

        try:
            page.goto(
                URL,
                wait_until="domcontentloaded",
                timeout=60_000,
            )

            # Playwright can automatically enter an open Shadow DOM.
            root = page.locator("#IREvents")
            root.wait_for(state="visible", timeout=30_000)

            # 1. Section heading: Upcoming Events
            section = root.locator("h1", has_text="Upcoming Events").first
            section_title = clean_text(section.inner_text())

            # 2. First upcoming event date and time
            date_element = root.locator(".c-caption.f-small").first
            event_datetime = clean_text(date_element.inner_text())

            # 3. First upcoming event title
            title_element = root.locator("h3").first
            event_title = clean_text(title_element.inner_text())

            return {
                "section": section_title,
                "datetime": event_datetime,
                "title": event_title,
            }

        finally:
            browser.close()


if __name__ == "__main__":
    event = extract_upcoming_event()

    print("Section:", event["section"])
    print("Date and time:", event["datetime"])
    print("Event title:", event["title"])