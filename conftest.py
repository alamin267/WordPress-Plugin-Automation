import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")  # reads from .env or CI secret

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=bool(os.getenv("CI", "true").lower() == "false")
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, base_url):
    context = browser.new_context()
    page = context.new_page()
    if base_url:
        page.goto(base_url)  # opens app url if available
    yield page
    context.close()
