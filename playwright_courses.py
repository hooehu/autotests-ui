from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Веб-элементы
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')

    # Заполняем поля ввода
    email_input.fill('user@gmail.com')
    username_input.fill('username')
    password_input.fill('password')

    # Кликаем по кнопке регистрации
    expect(registration_button).not_to_be_disabled()
    registration_button.click()

    context.storage_state(path='browser-state1.json')

    # Создаем вторую сессию браузера
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(storage_state='browser-state1.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Веб-элементы
    elements_to_check = [
    page.get_by_test_id('courses-list-toolbar-title-text'),
    page.get_by_test_id('courses-list-empty-view-icon'),
    page.get_by_test_id('courses-list-empty-view-title-text'),
    page.get_by_test_id('courses-list-empty-view-description-text')
    ]

    # Проверяем видимость веб-элементоу на странице
    for element in elements_to_check:
        expect(element).to_be_visible()

    page.wait_for_timeout(5000)