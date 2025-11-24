import pytest
import re
import logging
from playwright.sync_api import Playwright, expect

from pages.home_page import *
from utils.playwright_utilities import *

logger = logging.getLogger(__name__)

@pytest.mark.all_tests
def test_home_page(playwright: Playwright) -> None:
    browser_instance = get_browser_instance(playwright)
    context = get_context(browser_instance)
    page = get_page(context)

    logger.info("Starting Home page test")
    navigate_to_me(page)

    # Check page has title
    expect(page).to_have_title(re.compile("Software Quality Assurance & Testing"))

    logger.info("Ending Home page test")

    # Stop tracing, close browser instance, close context
    end_open_session(context, browser_instance)

#  playwright codegen https://sqa.stackexchange.com/
#  pytest -m all_tests
