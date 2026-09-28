import re

from playwright.sync_api import Page

from elements.button import Button
from elements.text import Text
from components.base_component import BaseComponent


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(
            page=page,
            locator='courses-list-toolbar-title-text',
            name='Toolbar text'
        )
        self.create_course_button = Button(
            page=page,
            locator='courses-list-toolbar-create-course-button',
            name='Create course button'
        )

    def check_visible(self) -> None:
        self.title.check_visible()
        self.title.check_have_text('Courses')
        self.create_course_button.check_visible()

    def click_course_button(self) -> None:
        self.create_course_button.click()
        self.check_current_url(re.compile(r".*/#/courses/create"))

