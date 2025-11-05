import pytest
import re
import logging
from playwright.sync_api import Page, expect

from pages.home_page import navigate_to_me

logger = logging.getLogger(__name__)


@pytest.mark.all_tests
def test_home_page_has_title(page: Page) -> None:
    logger.info("Starting test to check Home page title")
    navigate_to_me(page)
    #page.screenshot(path="reports/screenshots/home.png")

    # Check page title
    expect(page).to_have_title(re.compile("Software Quality Assurance & Testing"))

    logger.info("Ending test to check Home page title")

    """
    need to use BrowserContext
    context = browser.new_context()
    context.close()
    browser.close()
    then do the same for test_questions_page
    """
