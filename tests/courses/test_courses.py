import re

import allure
import pytest

from tools.allure.tags import AllureTag
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage) -> None:
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible('username')
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage) -> None:
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_toolbar_view_component.check_visible()

        create_course_page.image_upload_widget_component.check_visible(is_image_uploaded=False)

        create_course_page.create_course_form_component.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )

        create_course_page.create_course_exercises_toolbar_view_component.check_visible()

        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget_component.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget_component.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form_component.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_form_component.check_visible(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=False)

        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        courses_list_page.check_current_url(re.compile(r'.*/#/courses$'))
        courses_list_page.toolbar_view.check_visible()

        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
        )

    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage) -> None:
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_form_component.fill(
            title='Course title',
            estimated_time='1 day',
            description='Test course',
            max_score='100',
            min_score='10'
        )
        create_course_page.image_upload_widget_component.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        courses_list_page.check_current_url(re.compile(r'.*/#/courses$'))
        courses_list_page.course_view.check_visible(
            index=0,
            title='Course title',
            max_score='100',
            min_score='10',
            estimated_time='1 day'
        )
        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form_component.check_visible(
            title='Course title',
            estimated_time='1 day',
            description='Test course',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_form_component.fill(
            title='Updated course title',
            estimated_time='2 days',
            description='Updated course description',
            max_score='90',
            min_score='20'
        )
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        courses_list_page.check_current_url(re.compile(r'.*/#/courses$'))
        courses_list_page.course_view.check_visible(
            index=0,
            title='Updated course title',
            max_score='90',
            min_score='20',
            estimated_time='2 days'
        )
