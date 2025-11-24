from playwright.sync_api import Page, Locator
from namespace_urls.namespace_urls import BASE_URL

"""Home page"""

page_url = BASE_URL

def navigate_to_me(page: Page) -> None:
    page.goto(BASE_URL)

def loaded_successfully(page: Page) -> Locator:
    return page.get_by_text("Software Quality Assurance & Testing").first

