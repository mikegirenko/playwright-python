import re
from playwright.sync_api import Page, expect

from pages.home_page import navigate_to_me


def test_home_page_has_title(page: Page):
    navigate_to_me(page)
    page.screenshot(path="reports/screenshots/home.png")

    # Expect title "to contain" a substring.
    expect(page).to_have_title(re.compile("Software Quality Assurance & Testing"))
