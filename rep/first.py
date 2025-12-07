import time

from playwright.sync_api import sync_playwright, expect

from playwright_registration import username_input

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input1 = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registrtion_button = page.get_by_test_id('registration-page-registration-button')

    email_input.fill('user.name@gmail.com')
    username_input1.fill('username')
    password_input.fill('password')
    header = page.get_by_test_id('dashboard-toolbar-title-text')

    expect(registrtion_button).to_be_enabled()
    registrtion_button.click()
    expect(header).to_be_visible()
    time.sleep(5)


