import pytest
from playwright.sync_api import expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Добавили проверку Navbar компонента на странице CoursesListPage
    courses_list_page.navbar.check_visible(username="username")
    # Добавили проверку Sidebar компонента на странице CoursesListPage
    courses_list_page.sidebar.check_visible()

    courses_list_page.check_visible_courses_title()

    courses_list_page.check_visible_empty_view()

    courses_list_page.check_visible_create_course_button()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    # Проверяем страницу создания курса
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0"
    )

    # Проверяем блоки создания заданий
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    # Заполняем данные курса и создаем его
    create_course_page.upload_preview_image('./testdata/files/image.jpg')
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form('Playwright', '2 weeks', 'Playwright', '100', '10')
    create_course_page.click_create_course_button()

    # Проверяем данные созданного курса
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )
