from playwright.sync_api import Locator, Page, expect


class BaseElement:
    # name - под аллюр + читабельность
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    # Билдим локатор
    def get_locator(self,nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)

    # Универсальные методы элементов
    def click(self, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
