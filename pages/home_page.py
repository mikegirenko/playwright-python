"""Home page"""

from playwright.sync_api import Page, Locator
from namespace_urls.namespace_urls import BASE_URL

page_url = BASE_URL

def navigate_to_me(page: Page) -> None:
    page.goto(page_url)


def loaded_successfully(page: Page) -> Locator:
    return page.get_by_text("Software Quality Assurance & Testing")
