from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_email_input.clear()
        self.registration_username_input.clear()
        self.registration_password_input.clear()
        self.registration_email_input.fill(email)
        self.registration_username_input.fill(username)
        self.registration_password_input.fill(password)

    def click_registration_button(self):
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()


