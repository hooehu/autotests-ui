# Импортируем PLaywright
from playwright.sync_api import sync_playwright, expect

# expect - функция из Playwright, которая позволяет писать ассерты (проверки)
# sync_playwright - функция для запуска Playwright в синхронном режиме

# Данная конструкция с with - контекстный менеджер. Он нужен для закрытия браузера после вызода из контекстного менеджера
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False) # headless - запуск с отображением UI

    # Создание новой страницы
    page = browser.new_page()

    # Открываем страницу в браузере
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Поиск локаторов в DOM-е
    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    password_input = page.get_by_test_id('login-form-password-input').locator('//div//input')
    # Поиск сразу по data-testid (если таковой есть)
    login_button = page.get_by_test_id('login-page-login-button')
    alert = page.locator('//div[@data-testid = "login-page-wrong-email-or-password-alert"]')

    # Заполнение инпуов данными
    email_input.fill('hooehu')
    password_input.fill('qwerty123')

    # Неявное ожидание
    page.wait_for_timeout(1500)

    # Нажатие кнопки "Login"
    login_button.click()
    page.wait_for_timeout(3000)
    # Проверяем, что на странице отображается алерт об ошибки авторизации
    expect(alert).to_be_visible()

    # Проверка элемента по содержанию текста на странице
    expect(alert).to_have_text('Wrong email or password')