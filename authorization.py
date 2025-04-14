from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполняем поле email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # Заполняем поле password
    pass_input = page.get_by_test_id('login-form-password-input').locator('input')
    pass_input.fill('password')

    # Нажимаем на кнопку Login
    login_btn = page.get_by_test_id('login-page-login-button')
    login_btn.click()

    # Проверяем, что появилось сообщение об ошибке
    error_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(error_alert).to_be_visible()
    expect(error_alert).to_have_text("Wrong email or password")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(2000)