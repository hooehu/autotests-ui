import pytest

# Автоматически запускается перед тестом без необходимости ее передавать
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUOTOUSE] Отправляем данные в сервис аналитики")

# Запускается 1 раз на всю тестовую сессию
@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки автотеста")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя на 1 тестовый класс")

# Запускается для конкретной функции. Если скоуп не указан, то используется по умолчанию
@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Открываем браузер на каждый автотест")

# Запускатеся для файлов, в директории которых есть файл __init__.py
@pytest.fixture(scope="package")
def asas():
    pass

# Запускатеся для одного конкретного файла
@pytest.fixture(scope="module")
def settings2():
    pass


# Смотрим, как работают фикстуры

class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass
