from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # Создали контекст
    context = browser.new_context(storage_state="browserState.json")
    # Создаем страницу
    page = context.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard",
        wait_until="networkidle"
              )

    # email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    # email_input.fill('user.name@gmail.com')
    #
    # username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    # username_input.fill('username')
    #
    # password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    # password_input.fill('password')
    #
    # registration_button = page.get_by_test_id('registration-page-registration-button')
    # registration_button.click()


    #storage = context.storage_state(path="output/browserState.json")

