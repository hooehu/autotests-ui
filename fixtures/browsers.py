from collections.abc import Generator

import pytest
from playwright.sync_api import Page, Playwright, expect


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        yield page
    finally:
        browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    try:
        context = browser.new_context()
        page = context.new_page()
        page.goto(
            'https://nikita-filonov.github.io/'
            'qa-automation-engineer-ui-course/#/auth/registration'
        )

        email_input = page.get_by_test_id(
            'registration-form-email-input'
        ).locator('input')
        username_input = page.get_by_test_id(
            'registration-form-username-input'
        ).locator('input')
        password_input = page.get_by_test_id(
            'registration-form-password-input'
        ).locator('input')
        registration_button = page.get_by_test_id(
            'registration-page-registration-button'
        )
        h6_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')

        email_input.fill('user@gmail.com')
        username_input.fill('username')
        password_input.fill('password')

        expect(registration_button).not_to_be_disabled()
        registration_button.click()

        expect(h6_dashboard).to_be_visible()
        print('Регистрация пользователя прошла успешно!')

        context.storage_state(path='browser-state.json')
    finally:
        browser.close()


@pytest.fixture()
def chromium_page_with_state(
    initialize_browser_state: None,
    playwright: Playwright
) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    try:
        yield page
    finally:
        browser.close()
