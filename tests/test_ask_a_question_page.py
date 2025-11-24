import pytest
import re
import logging
from playwright.sync_api import Playwright, expect

from pages.questions_page import navigate_to_me
from utils.playwright_utilities import *

logger = logging.getLogger(__name__)

def test_ask_question_button(playwright: Playwright) -> None:
    browser_instance = get_browser_instance(playwright)
    context = get_context(browser_instance)
    page = get_page(context)

    logger.info("Starting test to check Ask Question button")
    navigate_to_me(page)

    # Click the Ask Question button.
    page.get_by_role("link", name="Ask Question", exact=True).click()

    # Check page "Ask a public question" text.
    expect(page.get_by_text("Ask a public question")).to_be_visible()
    #  page.wait_for_timeout(5000)

    logger.info("Ending test to check Questions page title")

    end_open_session(context, browser_instance)
