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

    # Confirm Explore our questions table is not blank (has at least one non-whitespace character)
    expect(explore_our_questions_table(page)).to_contain_text(re.compile(r"\S"))
    expect(sidebar(page)).to_contain_text(re.compile(r"\S"))

    # Confirm Hot Network Questions section exists and populated
    expect(hot_network_questions(page)).to_be_visible()

    logger.info("Ending Home page test")

    # Stop tracing, close browser instance, close context
    end_open_session(context, browser_instance)


#  pytest -m all_tests
