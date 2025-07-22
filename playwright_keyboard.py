from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')

    # Ставим фокус на веб-элемент
    email_input.focus()

    for char in 'user@gmail.com':
        # Заоплняем инпут веб-элемента символами с задержкой для наглядности
        page.keyboard.type(char, delay=130)

    # Cmd + A с клавиатуры
    page.keyboard.press('ControlOrMeta+A')
    page.wait_for_timeout(2000)

