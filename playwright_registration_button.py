from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Веб-элементы
    registration_button = page.get_by_test_id('registration-page-registration-button')
    email_input = page.locator('//div[@data-testid="registration-form-email-input"]/div/input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('//div/input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('//div/input')
    registration_button = page.get_by_test_id('registration-page-registration-button')

    # Проверка неактивности кнопки регистрации
    expect(registration_button).to_be_disabled()

    # Заполнение полей
    email_input.focus()
    for char in 'user.name@gmail.com':
        page.keyboard.press(char, delay=100)

    username_input.fill('username')
    password_input.fill('password')

    # Проверка доступности кнопки регистрации
    expect(registration_button).to_be_enabled()


