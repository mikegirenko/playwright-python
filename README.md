Playwright, Python, pytest.

Things I like about Playwright:
1. Can run tests on many browsers, OS, headed and headless, with mobile emulation
2. It works great with pytest
3. Built-in wait before taking an action against UI, and it actually works. No more custom build dynamic waits!
4. Built-it wait before performing an assertion. MG 12-24-2025: Built-in wait is good, but not perfect. I have one test, 
   which has ine assertion, which fails randomly. Test can run 40 times in a loop without failure, then fail. It is not 
   related to unstable environment, not related to test data, not related to previous action triggering UI change. I was 
   able to solve it by adding additional "expect" line before this assertion, but it feels strange
5. Good amount of built-in locators
6. Good amount of auto-retrying assertions that remove flakines
7. Good list of basic actions (click, hover, fill)
8. Browser Context is nice to keep tests clean and isolated. Can use Page instead, if needed
9. codegen is nice and helps with code generation, can record assertions, and understand locators
10. Playwright tracing is nice, it is recording a trace before performing actions, then at the end saves it to a file
11. Because Playwright using pytest, can easily save and view reports (xml, html, allure) 
12. "Playwright tests can be run on any CI provider", per Playwright. I have not tried it. I also not sure if I want to 
run slow UI test as a part of CI pipeline. A some type of scheduled job would be better
13. Tests can be debugged using PWDEBUG command, which will open browser window and Playwright Inspector
