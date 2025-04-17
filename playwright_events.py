from playwright.sync_api import sync_playwright, Request, Response

def log_request(request: Request):
    print(f'Request: {request.url}')

def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    listener = lambda request: print(f'Request: {request.url}')

    page.on('request', listener)
    page.on('response', log_response)

    page.wait_for_timeout(2000)
