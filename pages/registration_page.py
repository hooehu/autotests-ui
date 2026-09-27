from playwright.sync_api import Page

from components.authentication.registration_form_component import (
    RegistrationFormComponent,
)
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form_component = RegistrationFormComponent(page)
        self.registration_button = Button(
            page=page,
            locator='registration-page-registration-button',
            name='Registration button'
        )
        self.login_link = Link(
            page=page,
            locator='registration-page-login-link',
            name='Login link'
        )

    def click_registration_button(self) -> None:
        self.registration_button.check_enabled()
        self.registration_button.click()

    def click_login_link(self) -> None:
        self.login_link.click()
