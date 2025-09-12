from playwright.sync_api import Page
"""
Playwright specific functions:
start_session
navigate_to_page
"""

def navigate_to_page(page: Page, page_url):
    page.goto(page_url)
