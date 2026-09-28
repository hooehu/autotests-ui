from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(
            page=page,
            locator="course-view-menu-button",
            name='Menu button'
        )
        self.edit_button = Button(
            page=page,
            locator="course-view-edit-menu-item",
            name='Edit button'
        )
        self.delete_button = Button(
            page=page,
            locator="course-view-delete-menu-item",
            name='Delete button'
        )

    def click_edit(self, index: int, nth: int = 0):
        self.menu_button.click(nth=index)
        self.edit_button.check_visible(nth=index)
        self.edit_button.click(nth=index)

    def click_delete(self, index: int):
        self.delete_button.click(nth=index)
        self.delete_button.check_visible(nth=index)
        self.delete_button.click(nth=index)