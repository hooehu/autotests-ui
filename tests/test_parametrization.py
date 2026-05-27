import pytest
from _pytest.fixtures import SubRequest

# Нужно проверить, что числа 1, 2, 3, -1 больше 0
'''
Первый параметр - название параметризированного параметра
Второй параметр - указываем список (или туплом) тех параметров, которыми мы хотим параметризировать тест

Далее название парамтризированного параметра передаем в сам тест (Желательно с аннотацией)

Сам тест будет запущен 4 раза. На каждом запуске будет применено одно из значений
Если один из тестов упадет, то оставшиеся все равно запустятся
'''

@pytest.mark.parametrize("number", [-1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

# Для двух динамически изменяемых аргументов
@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)] )
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

# Перемножение (Пр:  запуск теста на разных ОС в разных браузерах) - запустится 12 тестов
@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


# Параметризация фикстур
'''
request - системный аргумент, который pytest передает в каждую фикстуру
В этом аргументе хранится разная мета инфа, а также параметр, которым параметризирована текущая фикстура

Не забываемпро импорт from _pytest.fixtures import SubRequest

.param хранит в себе какое то из этих значений params=["chromium", "webkit", "firefox"]
'''
@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request: SubRequest):
    return request.param

# Пройдет 3 теста на 3 разных браузерах из params в фикстуре
def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")


# Использование параметризации для тестового класса
@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations: {user}')

    def test_user_without_operations(self, user):
        print(f'User without operations: {user}')

# Использование идентификаторов для удобства чтения вывода
# создадим словарь для пользователей
users = {
    '+79211234567': 'User with money on bank account',
    '+79211234568': 'User without money on bank account',
    '+79211234569':  'User with operations on bank account'
}
@pytest.mark.parametrize(
    'phone_number',
    #Возвращаем ключи (номера тф)
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
            )
def test_identifiers(phone_number):
    pass