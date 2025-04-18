import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Открываем браузер и создаем новую страницу
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Переходим на страницу авторизации
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Заполняем поля: "Email", "Username", "Password"

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('user2.name@gmail.com')

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill('username2')

        reg_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        reg_password_input.fill('password123')

        # Доп проверка на активность кнопки "Registration"

        registration_button = page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_enabled()

        # Нажимаем на кнопку "Registration", после чего произойдет редирект на страницу Dashboard
        registration_button.click()

        # Проверяем, что на странице "Dashboard" отображается заголовок "Dashboard"
        dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()
        expect(dashboard_title).to_have_text('Dashboard')

        context.storage_state(path='browser_state.json')


    with sync_playwright() as playwright:
        # Открываем браузер и создаем новую страницу
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser_state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
        courses_toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_list_title).to_be_visible()
        expect(courses_list_title).to_have_text('There is no results')
        expect(courses_toolbar_title).to_be_visible()
        expect(courses_toolbar_title).to_have_text('Courses')
        page.wait_for_timeout(3000)