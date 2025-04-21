import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password(chromium_page: Page):
        # Переходим на страницу входа
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Заполняем поле email
        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        # Заполняем поле password
        pass_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        pass_input.fill('password')

        # Нажимаем на кнопку Login
        login_btn = chromium_page.get_by_test_id('login-page-login-button')
        login_btn.click()

        # Проверяем, что появилось сообщение об ошибке
        error_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(error_alert).to_be_visible()
        expect(error_alert).to_have_text("Wrong email or password")

        # # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
        # chromium_page.wait_for_timeout(2000)