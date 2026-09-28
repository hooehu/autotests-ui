from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import TextArea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(
            page=page,
            locator='create-course-form-title-input',
            name='Title input'
        )
        self.estimated_time_input = Input(
            page=page,
            locator='create-course-form-estimated-time-input',
            name='Estimated time input'
        )
        self.description_textarea = TextArea(
            page=page,
            locator='create-course-form-description-input',
            name='Description textarea'
        )
        self.max_score_input = Input(
            page=page,
            locator='create-course-form-max-score-input',
            name='Max score input'
        )
        self.min_score_input = Input(
            page=page,
            locator='create-course-form-min-score-input',
            name='Min score input'
        )

    def fill(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str
    ) -> None:
        self.title_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    def check_visible(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str
    ) -> None:
        self.title_input.check_visible()
        self.estimated_time_input.check_visible()
        self.description_textarea.check_visible()
        self.max_score_input.check_visible()
        self.min_score_input.check_visible()

        self.title_input.check_have_value(title)
        self.estimated_time_input.check_have_value(estimated_time)
        self.description_textarea.check_have_value(description)
        self.max_score_input.check_have_value(max_score)
        self.min_score_input.check_have_value(min_score)
