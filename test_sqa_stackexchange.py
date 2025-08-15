"""
--Install the Pytest plugin: pip install pytest-playwright
--Install the required browsers: playwright install
I do not need to do this because I have pyenv, and it already has the above
"""

import re
from playwright.sync_api import Page, expect

BASE_URL = "https://sqa.stackexchange.com"

def test_has_title(page: Page):
    page.goto(BASE_URL)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Software Quality Assurance & Testing Stack Exchang"))

def test_get_started_link(page: Page):
    page.goto(BASE_URL)

    # Click the Questions link.
    page.get_by_role("link", name="Questions", exact=True).click()

    # Expects page to have a heading with the name of Newest Questions.
    expect(page.get_by_role("heading", name="Newest Questions")).to_be_visible()
