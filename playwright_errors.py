from playwright.sync_api import sync_playwright, Request, Response, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')


    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')
    title_new_text = 'New Title'

    page.evaluate("""
           (title_new_text) => {
               const title = document.getElementById('authentication-ui-course-title-text');
               title.textContent = title_new_text
           }
           """,
                  title_new_text)
