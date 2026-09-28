from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(
            page=page,
            locator=f'{identifier}-empty-view-icon',
            name='Empty view icon'
        )
        self.title = Text(
            page=page,
            locator=f'{identifier}-empty-view-title-text',
            name='Empty view title'
        )
        self.description = Text(
            page=page,
            locator=f'{identifier}-empty-view-description-text',
            name='Empty view description'
        )

    def check_visible(
        self,
        title: str,
        description: str
    ) -> None:
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)
