from collections.abc import Generator

import pytest
from playwright.sync_api import Page, Playwright, expect

from pages.authentication.registration_page import RegistrationPage


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

    context = browser.new_context()
    page = context.new_page()
    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form_component.fill(email='test@test.ru', username='username', password='qwerty')
    registration_page.click_registration_button()
    context.storage_state(path='browser-state.json')


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
