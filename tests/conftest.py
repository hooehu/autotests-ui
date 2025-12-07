# Файл для фикстур. Обязательно должен называться conftest

import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="function")
# Аннотация -> Page указывает какой тип данных будет получен / возвращен
def chromium_page() -> Page:
    # Действия до теста
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # Сам код теста
        yield browser.new_page()
        # Дествия после теста
        print('Фиксстура применена успешно!')


