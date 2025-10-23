from playwright.sync_api import Playwright, expect

"""
Two pages using each own context (results in two browser instances). This test wil take more time because of browser 
opening and closing but will work great when tests need independent session data (cookies, local storage, and cache).
Test execution times are 4.27s, 4.90s, 4.87s
"""

def test_pages_not_sharing_context(playwright:Playwright):
    browser_one = playwright.chromium.launch(headless=False)
    context_one = browser_one.new_context() # Create one browser context

    page_one = context_one.new_page() # use first browser context
    page_one.goto('https://playwright.dev/python/')
    expect(page_one.get_by_role("link", name="Get started")).to_be_visible()

    context_one.close()
    browser_one.close()

    browser_two = playwright.chromium.launch(headless=False)
    context_two = browser_two.new_context() # Create second browser context

    page_two = context_two.new_page()  # use second browser context
    page_two.goto('https://sqa.stackexchange.com')
    expect(page_two.get_by_role("link", name="Ask Question")).to_be_visible()

    context_two.close()
    browser_two.close()
