from playwright.sync_api import sync_playwright, expect, Request, Response

# callback функция, обрабатывающая request
def log_request(request: Request):
    print(f'Request: {request.url}')

# Аналогично для ответа
def log_response(response: Response):
    print(f'Response: {response.url}')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Метод ".on" принимает 2 агрумента: само событие и callback ф-ция

    # Перехватываем запрос
    page.on('request', log_request)

    # Удаляем обработчик. Например, если нужны только ответы от сервера
    page.remove_listener('request', log_request)

    # Перехватываем ответ
    page.on('response', log_response)

    page.wait_for_timeout(4000)