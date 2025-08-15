"""Home page"""

from playwright.sync_api import Page, Locator

from common.common import BASE_URL

my_url = BASE_URL


def navigate_to_me(page: Page) -> None:
    page.goto(my_url)


def loaded_successfully(page: Page) -> Locator:
    return page.get_by_text("Software Quality Assurance & Testing")
