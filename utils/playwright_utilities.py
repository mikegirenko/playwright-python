from playwright.sync_api import Page
"""
Playwright specific functions:
start_session()
navigate_to_page()
"""

def navigate_to_page(page: Page, page_url):
    page.goto(page_url)


# def navigate_to_page(user: BrowserContext, page_object: types.ModuleType) -> Page:
#     """Navigate to the page represented by the page object passed in."""
#
#     if not hasattr(page_object, "navigate_to_me") or not hasattr(page_object, "loaded_successfully"):
#         raise RuntimeError(f"The page object {page_object} needs both navigate_to_me and loaded_successfully")
#
#     # Start with this user's most recent page
#     page = user.pages[0]
#
#     go_to_page_with_retries(page, page_object)
#
#     return page