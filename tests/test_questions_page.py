import pytest
import re
import logging
from playwright.sync_api import Playwright, expect

from pages.questions_page import *
from utils.playwright_utilities import *

logger = logging.getLogger(__name__)

@pytest.mark.all_tests
def test_questions_page(playwright: Playwright) -> None:
    browser_instance = get_browser_instance(playwright)
    context = get_context(browser_instance)
    page = get_page(context)

    logger.info("Starting Questions page test")
    navigate_to_me(page)
    page.screenshot(path="reports/screenshots/newest_questions.png")

    # Check page has title
    expect(page).to_have_title(re.compile("Newest Questions"))

    # Check questions count is not null
    questions_count_with_text = questions_count(page).inner_text().split(' ')
    numbers_only = questions_count_with_text[0]

    assert numbers_only is not None

    logger.info("Ending Questions page test")

    end_open_session(context, browser_instance)
