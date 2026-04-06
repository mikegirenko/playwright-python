from playwright.sync_api import Page, Locator, expect
from namespace_urls.namespace_urls import BASE_URL

"""Home page"""

page_url = BASE_URL

def navigate_to_me(page: Page) -> None:
    page.goto(BASE_URL)
    expect(page.get_by_role("link", name="Software Quality Assurance &").first).to_be_visible()

def page_title(page: Page) -> Locator:
    return page.get_by_role("link", name="Software Quality Assurance &").first

def explore_our_questions(page: Page) -> Locator:
    return page.get_by_role("heading", name="Explore our questions")

def explore_our_questions_table(page: Page) -> Locator:
    return page.locator("#mainbar")
