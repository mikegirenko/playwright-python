"""
--Install the Pytest plugin: pip install pytest-playwright
--Install the required browsers: playwright install
I do not need to do this because I have pyenv, and it already has the above
"""

import re
from playwright.sync_api import Page, expect

from common.common import BASE_URL
from pages.questions_page import navigate_to_me


def test_questions_page_has_title(page: Page) -> None:
    navigate_to_me(page)
    page.screenshot(path="reports/screenshots/newest_questions.png")

    # Expect title "to contain" a substring.
    expect(page).to_have_title(re.compile("Newest Questions"))

def test_ask_question_button(page: Page) -> None:
    navigate_to_me(page)

    # Click the Ask Question button.
    page.get_by_role("link", name="Ask Question", exact=True).click()

    # Expects page to have a heading with the name of Newest Questions.
    expect(page.get_by_role("heading", name="Asking a good question")).to_be_visible()
    #page.wait_for_timeout(5000)
