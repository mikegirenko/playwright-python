import logging
import pytest
from playwright.sync_api import Page, expect, BrowserContext, Locator, Playwright

from test_data.hard_coded.hardcoded import *

"""
Playwright specific functions
"""

logger = logging.getLogger(__name__)

def get_browser_instance(playwright: Playwright) -> BrowserContext:
    browser = BROWSER
    headless = HEADLESS
    if browser == "chromium":
        browser_brand = playwright.chromium
    if browser == "firefox":
        browser_brand = playwright.firefox
    if browser == "webkit":
        browser_brand = playwright.webkit
    browser_instance = browser_brand.launch(headless=headless)

    return browser_instance

def get_context(browser_instance) -> BrowserContext:
    context = browser_instance.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    return context

def get_page(context) -> Page:
    page = context.new_page()

    return page

def end_open_session(open_context, open_browser_instance) -> None:
    open_context.tracing.stop(path="reports/trace/trace.zip")
    open_context.close()
    open_browser_instance.close()
