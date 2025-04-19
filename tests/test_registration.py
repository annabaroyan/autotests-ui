from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
        # Переходим на страницу авторизации
        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Заполняем поля: "Email", "Username", "Password"

        registration_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('user.name@gmail.com')

        registration_username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill('username')

        reg_password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        reg_password_input.fill('password')

        # Доп проверка на активность кнопки "Registration"

        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_enabled()

        # Нажимаем на кнопку "Registration", после чего произойдет редирект на страницу Dashboard
        registration_button.click()

        # Проверяем, что на странице "Dashboard" отображается заголовок "Dashboard"
        dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()
        expect(dashboard_title).to_have_text('Dashboard')


