import re

from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form_component = LoginFormComponent(page)

        # применяем пейдж фактори
        self.login_button = Button(page=page, locator='login-page-login-button', name='Login')
        self.registration_link = Link(page=page, locator='login-page-registration-link', name='Registration')
        self.wrong_email_or_password_alert = Text(
            page=page,
            locator='login-page-wrong-email-or-password-alert',
            name='Wrong email or password'
        )

    def click_login_button(self) -> None:
        self.login_button.click()

    def click_registration_link(self) -> None:
        self.registration_link.click()
        self.check_current_url(re.compile(r'.*/#/auth/registration'))

    def check_visible_wrong_email_or_password_alert(self) -> None:
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')
