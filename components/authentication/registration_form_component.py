from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(
            page=page,
            locator='registration-form-email-input',
            name='Registration email input'
        )
        self.username_input = Input(
            page=page,
            locator='registration-form-username-input',
            name='Registration username input'
        )
        self.password_input = Input(
            page=page,
            locator='registration-form-password-input',
            name='Registration password input'
        )

    def fill(self, email: str, username: str, password: str) -> None:
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def check_visible(
        self,
        email: str,
        username: str,
        password: str
    ) -> None:
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)
