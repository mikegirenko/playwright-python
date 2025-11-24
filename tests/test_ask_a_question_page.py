import pytest
import re
import logging
from playwright.sync_api import Playwright, expect

from pages.ask_a_question_page import *
from utils.playwright_utilities import *

logger = logging.getLogger(__name__)

@pytest.mark.all_tests
def test_ask_question_button(playwright: Playwright) -> None:
    browser_instance = get_browser_instance(playwright)
    context = get_context(browser_instance)
    page = get_page(context)

    logger.info("Starting Ask a Question page test")
    navigate_to_me(page)

    # Check page "Asking a good question" text.
    expect(page.get_by_role("heading", name="Asking a good question")).to_be_visible()

    logger.info("Ending Ask a Question page test")

    # Stop tracing, close browser instance, close context
    end_open_session(context, browser_instance)
