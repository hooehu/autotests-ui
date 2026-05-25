import pytest
from playwright.sync_api import sync_playwright, expect
@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Веб-элементы
    title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    icon_empty_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    title_empty_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    text_description_empty_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')

    # Проверяем видимость веб-элементоу на странице
    expect(title_courses).to_be_visible()
    expect(title_courses).to_have_text("Courses")
    expect(icon_empty_list).to_be_visible()
    expect(title_empty_list).to_be_visible()
    expect(title_empty_list).to_have_text("There is no results")
    expect(text_description_empty_list).to_be_visible()
    expect(text_description_empty_list).to_have_text("Results from the load test pipeline will be displayed here")





