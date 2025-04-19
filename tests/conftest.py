from typing import Any, Generator

import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright) -> Generator[Playwright, Any, None]:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()