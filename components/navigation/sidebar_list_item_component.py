from typing import Pattern

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.icon = Icon(
            page=page,
            locator='{identifier}-drawer-list-item-icon',
            name='Sidebar icon'
        )
        self.title = Text(
            page=page,
            locator='{identifier}-drawer-list-item-title-text',
            name='Sidebar title text'
        )
        self.button = Button(
            page=page,
            locator='{identifier}-drawer-list-item-button',
            name='Sidebar button'
        )

    def check_visible(self, title: str, identifier: str) -> None:
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

        self.button.check_visible(identifier=identifier)

    def navigate(self, expected_url: Pattern[str], identifier: str) -> None:
        self.button.click(identifier=identifier)
        self.check_current_url(expected_url)
