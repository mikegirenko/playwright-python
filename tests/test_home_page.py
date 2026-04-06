from logging import NullHandler

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
    expect(page_title(page)).to_be_visible()

    # Confirm Explore our questions section exists and populated
    expect(explore_our_questions(page)).to_be_visible()

    # Confirm Explore our questions table is not blank
    assert len(explore_our_questions_table(page).inner_text()) > 0

    logger.info("Ending Home page test")

    # Stop tracing, close browser instance, close context
    end_open_session(context, browser_instance)

#  playwright codegen https://sqa.stackexchange.com/
#  pytest -m all_tests
