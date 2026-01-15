from playwright.sync_api import Page, Locator
from namespace_urls.namespace_urls import BASE_URL

"""Questions page"""

page_url = BASE_URL + "/questions"

def navigate_to_me(page: Page) -> None:
    page.goto(page_url)

def loaded_successfully(page: Page) -> Locator:
    return page.get_by_text("Newest Questions")

def questions_count(page: Page) -> Locator:
    return page.locator('.fs-body3').filter(has_text="questions")
