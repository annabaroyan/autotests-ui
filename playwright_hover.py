from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    registration_link = page.get_by_test_id('login-page-registration-link')

    registration_link.hover()

    page.evaluate("""
        (style) => {
            const reg_link = document.getElementById('login-page-registration-link')
            reg_link.style.border = style
        }
    """, '1px solid red')



    page.wait_for_timeout(2000)