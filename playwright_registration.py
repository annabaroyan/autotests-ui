from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Заполняем поля: "Email", "Username", "Password"

    reg_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    reg_email_input.fill('user.name@gmail.com')

    reg_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    reg_username_input.fill('username')

    reg_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    reg_password_input.fill('password')

    # Доп. проверка на активность кнопки "Registration"

    reg_btn = page.get_by_test_id('registration-page-registration-button')
    expect(reg_btn).is_enabled()

    # Нажимаем на кнопку "Registration", после чего произойдет редирект на страницу Dashboard
    reg_btn.click()

    # Проверяем, что на странице "Dashboard" отображается заголовок "Dashboard"
    dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard).to_be_visible()
    expect(dashboard).to_have_text('Dashboard')

