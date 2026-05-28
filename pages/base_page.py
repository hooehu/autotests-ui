from playwright.sync_api import Page
# Создаем класс для базовых операций, применимых ко всем страницам
class BasePage:
    # Конструктор
    def __init__(self, page: Page):
        self.page = page

    # Открытие страницы
    def visit(self, url: str):
        # Обращаемся к атрибуту page и применяем метод goto(), в который передаем url
        self.page.goto(url, wait_until='networkidle')
    # Перезагрузка страницы
    def reload(self, url: str):
        self.page.reload(wait_until='networkidle')