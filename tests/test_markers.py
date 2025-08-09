import pytest

"""
                    Маркировка функции. 
Для выбора по маркировки используем флаг -m "{название тега}"
Для запуска тестов по нескольким маркировкам: -m "{тег_1 or тег_2}"
Для запуска тестов с двумя тегами используется оператор "and "

"""
@pytest.mark.smoke
def test_smoke_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...


#Маркировка класса

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...
    @pytest.mark.slow
    def test_password_reset(self):
        ...
    def test_logout(self):
        ...

# Можно использовать -m "smoke and regression and critical"
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...