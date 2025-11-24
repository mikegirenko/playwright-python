from playwright.sync_api import Page, Locator
from namespace_urls.namespace_urls import BASE_URL

"""Ask a Question page"""

page_url = BASE_URL + "/questions"

def navigate_to_me(page: Page) -> None:
    """Accessing this page by clicking on the Ask Question button"""
    page.goto(page_url)
    # Click the Ask Question button.
    page.get_by_role("link", name="Ask Question", exact=True).click()


def loaded_successfully(page: Page) -> Locator:
    return page.get_by_text("Ask a Question")
