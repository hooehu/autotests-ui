import pytest
from playwright.sync_api import sync_playwright, Page, expect, Playwright


@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Локаторы
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_button = page.get_by_test_id('registration-page-registration-button')
        h6_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')

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

        context.storage_state(path='browser-state.json')

@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    yield page

    browser.close()