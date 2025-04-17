from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
              wait_until='networkidle')

    title_new_text = 'New Title'

    # page.evaluate(f"""
    # const title = document.getElementById('authentication-ui-course-title-text');
    # title.textContent = '{title_new_text}'
    # """)

    page.evaluate("""
        (title_new_text) => {
            const title = document.getElementById('authentication-ui-course-title-text');
            title.textContent = title_new_text
        }
        """,
        title_new_text)

    page.wait_for_timeout(1000)
