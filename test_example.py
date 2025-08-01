"""
--Install the Pytest plugin: pip install pytest-playwright
--Install the required browsers: playwright install
I do not need to do this because I have pyenv, and it already has the above
"""

import os
import re
from distutils.util import strtobool
from playwright.sync_api import BrowserContext, Locator, Page, Playwright, expect

# def start_session(playwright: Playwright):
#     base_url = "https://playwright.dev/"
#     #headless = env_to_bool("HEADLESS")
#     browser = os.getenv("BROWSER", "chromium")
#     browser_brand = playwright.chromium
#     browser_instance = playwright.chromium.launch()
#     context_args = {
#         "base_url": base_url,
#         "user_agent": "Playwright Chromium Robot",
#     }
#     start_session(playwright)
#     context = browser_instance.new_context(**context_args)
#     page = context.new_page()
#     page.goto(base_url)
#
#
# def env_to_bool(environment_variable) -> bool:
#     return bool(strtobool(os.getenv(environment_variable, "false").lower()))

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    page.wait_for_timeout(2000)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")
#
#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()
#
#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()