import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.registration
@pytest.mark.regression
# Создаем тестовую фунцию для обертки самого написанного теста
def test_successful_registration(chromium_page: Page):

        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        h6_dashboard = chromium_page.get_by_test_id('dashboard-toolbar-title-text')

        # Заполняем поля ввода
        email_input.fill('user@gmail.com')
        username_input.fill('username')
        password_input.fill('password')

        # Кликаем по кнопке регистрации
        expect(registration_button).not_to_be_disabled()
        registration_button.click()

        # Проверяем наличие заголовка (успешная регистрация)
        expect(h6_dashboard).to_be_visible()
        print('Регистрация пользователя прошла успешно!')