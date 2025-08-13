import pytest
# Фикстура будет запускаться до теста автоматически

"""

При scope = "session" - фикстура будет запущена один раз за всю сессию
package - на всю папку, где лежит файл __init__.py
module - фиксутра будет запущена 1 раз для одного файла
class - фикстура будет запущена 1 раз на весь тестовый класс
function - фикстура будет запущена 1 раз на все тестовые функции

По умолчанию если написать @pytest.fixture() - используется scope = function

Мб autouse = True, scope = "class". Тогда autouse вызовется для каждого класса
"""

# Запускается автоматически без необходимсти ее передавать в тесты (функции)
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервисы аналитики")

# В консоли вызовется всего 1 раз на запуск 1 сесии
@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки АТ")

# В консоли вызовется 2 раза, так как у нас 2 класса
@pytest.fixture(scope="class")
def users():
    print("[CLASS] Создаем данные пользователя 1 раз на тестовый класс")

# В консоли вызовется 3 раза, так как у нас 3 функции
@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Открываем браузер на каждый АТ")


class TestUserFlow:
    """
    Передаем в аргументы функции фикстуру (функцию)
    Теперь каждый раз при вызове функции (теста) ниже перед этим будет выполняться переданная фикстура (функция)

    """
    def test_user_can_login(self, settings, users, browser):
        ...

    def test_user_can_create_course(self, settings, users, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, users, browser):
        ...
