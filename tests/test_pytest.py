# Pytest распознает все функции, которые начинаются с test_*
def test_user_login():
    print("Helllo!")


# Тоже начинаем название класса с Test*
class TestUserLogin:
    def test_1(self):
        ...

    def test_2(self):
        ...


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5, "Ошибка!"


"""
                    Флаги
1) -s: выводит результат
2) -v: добавляет доп инфу о выполнении тестов
3) -k "test_user": запускает определенный тест (в кавычках указыватся название класса/функции). Можно использовать 
логические выраженияя - or/and
 
"""
