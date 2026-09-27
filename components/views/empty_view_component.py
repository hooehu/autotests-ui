from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.icon = Icon(
            page=page,
            locator='{identifier}-empty-view-icon',
            name='Empty view icon'
        )
        self.title = Text(
            page=page,
            locator='{identifier}-empty-view-title-text',
            name='Empty view title'
        )
        self.description = Text(
            page=page,
            locator='{identifier}-empty-view-description-text',
            name='Empty view description'
        )

    def check_visible(
        self,
        title: str,
        description: str,
        identifier: str
    ) -> None:
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

        self.description.check_visible(identifier=identifier)
        self.description.check_have_text(description, identifier=identifier)
