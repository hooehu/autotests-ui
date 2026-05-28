from playwright.sync_api import sync_playwright, expect, Request, Response
import time
from http import HTTPStatus

def log_request(request: Request):
    print(f"Запрос {request.url}")

def log_response(response: Response):
    status = response.status
    print(f"Ответ {response.url} c кодос ответа {status}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent=None)

    # Обработчик событий
    page.on('request', log_request)
    page.on('response',log_response )


    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #locators
    email_input = page.get_by_test_id("registration-form-email-input").locator("//div/input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("//div/input")
    password_input = page.get_by_test_id("registration-form-password-input").locator("//div/input")
    register_button = page.get_by_test_id("registration-page-registration-button")
    h1 = page.get_by_test_id("dashboard-toolbar-title-text")
    login_button = page.get_by_test_id("registration-page-login-link")

    #Actions
    for character in "test@test.ru":
        email_input.press(character, delay=100)

    username_input.fill("tester")
    password_input.fill("tester")

    email_input.focus()
    page.keyboard.press("ControlOrMeta+A")
    page.wait_for_timeout(1000)

    expect(register_button).to_be_enabled()
    register_button.click()

    expect(h1).to_be_visible()
