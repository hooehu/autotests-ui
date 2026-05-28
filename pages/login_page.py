from pages.base_page import BasePage
from playwright.sync_api import Page, expect

# Создаем класс для отдельной страницы логина и наследуемся от класса BasePage
class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        # Указываем атрибуты класса
        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    # ! Название метода задается по принципу: Action(действие)-Context(с чем работаем)-Element_type(тип элемента)!
    # Метод заполнения полей регистрации
    def fill_login_form(self, email: str, password: str):
        # Заполняем поля
        self.email_input.fill(email)
        self.password_input.fill(password)
        # Проверяем, что поля заполены нужными значениями
        expect (self.email_input).to_have_value(email)
        expect (self.password_input).to_have_value(password)

    # Метод для клика на кнопку логина
    def click_login_button(self):
        # Кликаем на кнопку логина
        self.login_button.click()

    # Метод для клика на кнопку Регистрации
    def click_registration_link(self):
        self.registration_link.click()

    # Метод для проверки отображения алерта при ошибки регистрации
    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text('Wrong email or password')