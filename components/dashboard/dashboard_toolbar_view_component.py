from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(
            page=page,
            locator='dashboard-toolbar-title-text',
            name='Dashboard toolbar title'
        )

    def check_visible(self) -> None:
        self.title.check_visible()
        self.title.check_have_text('Dashboard')
