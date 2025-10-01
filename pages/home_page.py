# import types
from playwright.sync_api import Page, Locator
from utils.playwright_utilities import navigate_to_page
from namespace_urls.namespace_urls import BASE_URL

"""Home page"""

page_url = BASE_URL

def loaded_successfully(page: Page) -> Locator:
    return page.get_by_text("Software Quality Assurance & Testing").first

def navigate_to_me(page: Page) -> None:
    navigate_to_page(page, page_url)
    if loaded_successfully(page).all_text_contents() != ['Join Software Quality Assurance & TestingM']:
        raise RuntimeError("it failed")
    # if not hasattr(page_object, "navigate_to_me") or not hasattr(page_object, "loaded_successfully"):
    #     raise RuntimeError(f"The page object {page_object} needs both navigate_to_me and loaded_successfully")
    #print(loaded_successfully(page).all_text_contents())




