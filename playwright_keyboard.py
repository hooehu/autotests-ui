from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')

    # Ставим фокус на веб-элемент
    email_input.focus()

    for char in 'user@gmail.com':
        # Вводим каждый символ по отдельности. Задержка между вводом символов для наглядности
        page.keyboard.type(char, delay=190)

    # Применяем Cmd+A для выделения ввденного текста
    page.keyboard.press('ControlOrMeta+A')

    page.wait_for_timeout(2000)
