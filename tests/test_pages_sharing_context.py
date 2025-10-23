from playwright.sync_api import sync_playwright, expect

"""
Two pages share the same context (results in one browser instance with two tabs). This saves time on browser opening
and closing but will not work when tests need independent session data (cookies, local storage, and cache).
Test execution times are 3.90s, 3.65s, 3.68s
"""

def test_pages_sharing_context(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # Create a single browser context

    page_one = context.new_page() # use shared context
    page_one.goto('https://playwright.dev/python/')
    expect(page_one.get_by_role("link", name="Get started")).to_be_visible()

    page_two = context.new_page()  # use shared context
    page_two.goto('https://sqa.stackexchange.com')
    expect(page_two.get_by_role("link", name="Ask Question")).to_be_visible()

    context.close()
    browser.close()
