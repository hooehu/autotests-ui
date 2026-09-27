from playwright.sync_api import Locator, Page, expect


class BaseElement:
    # name - под аллюр + читабельность
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    # Билдим локатор
    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    # Универсальные методы элементов
    def click(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        locator.click()

    def check_visible(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
