import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        courses_toolbar_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_list_title).to_be_visible()
        expect(courses_list_title).to_have_text('There is no results')
        expect(courses_toolbar_title).to_be_visible()
        expect(courses_toolbar_title).to_have_text('Courses')
        chromium_page_with_state.wait_for_timeout(3000)