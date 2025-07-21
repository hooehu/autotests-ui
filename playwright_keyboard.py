from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    # Курсор на веб элемент
    email_input.focus()

    for char in 'user.name@gmail.com':
        page.keyboard.type(char, delay=180)

    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(2000)
