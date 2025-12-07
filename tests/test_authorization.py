import pytest
from playwright.sync_api import expect, Page, sync_playwright


@pytest.mark.authorization
@pytest.mark.regression
def test_authorization_error(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = chromium_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('//div//input')

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    alert = chromium_page.locator('//div[@data-testid = "login-page-wrong-email-or-password-alert"]')

    email_input.fill('hooehu')
    password_input.fill('qwerty123')

    chromium_page.wait_for_timeout(1500)

    login_button.click()
    chromium_page.wait_for_timeout(3000)

    expect(alert).to_be_visible()

    # Ждем алерт
    expect(alert).to_have_text('Wrong email or password')
