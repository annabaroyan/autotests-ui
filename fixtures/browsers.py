from typing import Any, Generator
import pytest
from playwright.sync_api import sync_playwright, Page, Playwright, expect


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
                'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')


        registration_email_input = page.get_by_test_id('registration-form-email-input').locator(
                'input')
        registration_email_input.fill('user2.name@gmail.com')

        registration_username_input = page.get_by_test_id(
                'registration-form-username-input').locator('input')
        registration_username_input.fill('username2')

        reg_password_input = page.get_by_test_id('registration-form-password-input').locator(
                'input')
        reg_password_input.fill('password123')


        registration_button = page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_enabled()

        registration_button.click()

        dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()
        expect(dashboard_title).to_have_text('Dashboard')

        context.storage_state(path='browser_state.json')
        browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Generator[Page, Any, None]:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser_state.json')
        yield context.new_page()
        browser.close()

