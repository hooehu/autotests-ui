from playwright.sync_api import sync_playwright, expect


def test_authorization_error():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

        email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        password_input = page.get_by_test_id('login-form-password-input').locator('//div//input')

        login_button = page.get_by_test_id('login-page-login-button')
        alert = page.locator('//div[@data-testid = "login-page-wrong-email-or-password-alert"]')

        email_input.fill('hooehu')
        password_input.fill('qwerty123')

        page.wait_for_timeout(1500)

        login_button.click()
        page.wait_for_timeout(3000)

        expect(alert).to_be_visible()

        # Ждем алерт
        expect(alert).to_have_text('Wrong email or password')