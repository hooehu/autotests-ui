import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:

    # Инициализация браузера
    browser = playwright.chromium.launch(headless=False)

    # Открытие url в новой вкладке
    page = browser.new_page()
    page.goto('http://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Объявление веб-элементов
    email_input = page.get_by_test_id('registration-form-email-input').locator('//div/input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('//div/input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('//div/input')
    registration_button = page.get_by_test_id('registration-page-registration-button')
    redirect_header = page.locator('//div[@class="MuiBox-root css-70qvj9"]/h6')

    # Заполнение инпутов
    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')

    # Проверка доступности кнопки и клик
    expect(registration_button).to_be_enabled()
    registration_button.click()

    # Проверка отображения заголовка после редиректа
    expect(redirect_header).to_be_visible()

