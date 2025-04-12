import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://www.saucedemo.com/v1/",
        help="Base URL for the application under test",
    )


@pytest.fixture(scope="session")
def headless(pytestconfig):
    return pytestconfig.getoption("--headless")


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--url")


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, headless):
    browser = playwright_instance.chromium.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture
def page(browser): 
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
