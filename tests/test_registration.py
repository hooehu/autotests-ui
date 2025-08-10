import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.registration
@pytest.mark.regression
# Создаем тестовую фунцию для обертки самого написанного теста
def test_successful_registration():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()

        ### Упрощение процесса авторизации в АТ. Чтобы каждый раз при запуске нового теста не проходила новая авторизация ###

        # Для сохранения куков и данных в session storage
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

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

        # Сохраняем состояние и указываем, куда мы его хотим сохранить (в json файл)
        # В результате получаем json файл с выгруженными данными из local storage
        context.storage_state(path='browser-state.json')

        # Запускаем новую сессию браузера
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        # Передаем файл в context из-за чего для браузера уже будут данные для авторизации
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        #page.wait_for_timeout(1500)