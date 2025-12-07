import pytest

@pytest.fixture()
def clear_books_database() -> None:
    print("[FIXTURE] Удаляем все данные из БД")

@pytest.fixture()
def fill_books_database() -> None:
    print("[FIXTURE] Создаем новы данные в БД")

"""
Позволяет вызвать фикстуру без autouse = True и без передачи фикстуры в аргументы теста (функции)
Так предпочтительно делать, когда фикстура не возвращает данных ( -> None) и когда autouse = True не подходит для использования
"""
@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print("Reading all books")

# Стоит учитывать порядок фикстур, если в тесте это важно
@pytest.mark.usefixtures('clear_books_database', 'fill_books_database')
class TestLibrary:

    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...