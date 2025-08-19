import pytest
import re
import logging
from playwright.sync_api import Page, expect

from pages.questions_page import navigate_to_me

logger = logging.getLogger(__name__)


@pytest.mark.all_tests
def test_questions_page_has_title(page: Page) -> None:
    logger.info("Starting test to check Questions page title")
    navigate_to_me(page)
    page.screenshot(path="reports/screenshots/newest_questions.png")

    # Check page title
    expect(page).to_have_title(re.compile("Newest Questions"))

    logger.info("Ending test to check Questions page title")


@pytest.mark.all_tests
def test_ask_question_button(page: Page) -> None:
    logger.info("Starting test to check Ask Question button")
    navigate_to_me(page)

    # Click the Ask Question button.
    page.get_by_role("link", name="Ask Question", exact=True).click()

    # Check page "Ask a public question" text.
    expect(page.get_by_text("Ask a public question")).to_be_visible()
    #  page.wait_for_timeout(5000)

    logger.info("Ending test to check Questions page title")

