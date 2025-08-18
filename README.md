Playwright, Python, pytest.

Things I like about Playwright:
1. Can run tests on many browsers, OS, headed and headless, with mobile emulation
2. It works great with pytest
3. Built-in wait before taking an action against UI, and it actually works. No more custom build dynamic waits!
4. Built-it wait before performing an assertion
5. Good amount of built-in locators
6. Good amount of auto-retrying assertions that remove flakines
7. Good list of basic actions (click, hover, fill)
8. Browser Context is nice to keep tests clean and isolated. But I still learning it
9. codegen is nice and helps with code generation, can record assertions, and understand locators
10. Because Playwright using Pytest plugin, when running test, it can record video and also can capture a screenshot
11. "Playwright tests can be run on any CI provider", per Playwright. I have not tried it. I also not sure if I want to run slow UI test as a part of CI pipeline
12. Tests can be debugged using PWDEBUG command, which will open browser window and Playwright Inspector