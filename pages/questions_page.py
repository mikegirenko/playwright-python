from playwright.sync_api import Page, Locator
from utils.playwright_utilities import navigate_to_page
from namespace_urls.namespace_urls import BASE_URL

"""Questions page"""

page_url = BASE_URL + "/questions"

def navigate_to_me(page: Page) -> None:
    navigate_to_page(page, page_url)


def loaded_successfully(page: Page) -> Locator:
    return page.get_by_text("Newest Questions")
