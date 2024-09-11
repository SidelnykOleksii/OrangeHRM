import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


@pytest.fixture(scope='class')
def browser(request) -> Page:
    """Provides a browser instance for testing based on configuration options.

    This fixture manages the lifecycle of a Playwright browser instance
    throughout the test class. It takes into account the `bn` pytest configuration
    option to determine which browser to launch (remote Chrome, Firefox, or local Chrome).

    Yields:
        playwright.sync_api.Page: A new browser page instance.
    """
    playwright = sync_playwright().start()
    if request.config.getoption("bn") == 'remote_chrome':
        browser = get_remote_chrome(playwright, request)
        context = get_context(browser, request, 'remote')
        page_data = context.new_page()
    elif request.config.getoption("bn") == 'firefox':
        browser = get_firefox_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
    elif request.config.getoption("bn") == 'chrome':
        browser = get_chrome_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
        context.tracing.start(snapshots=True, sources=True)
    else:
        browser = get_chrome_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        if request.config.getoption("bn") != 'remote_chrome':
            context.tracing.stop(path="C:/PythonPlaywrightStudy/OrangeHRM/trace.zip")
        context.close()
    browser.close()
    playwright.stop()


def get_firefox_browser(playwright, request) -> Browser:
    return playwright.firefox.launch(
        headless=request.config.getoption("h"),
        slow_mo=request.config.getoption("slow"),
    )


def get_chrome_browser(playwright, request) -> Browser:
    return playwright.chromium.launch(
        headless=request.config.getoption("h"),
        slow_mo=request.config.getoption("slow"),
        args=['--start-maximized']
    )


def get_remote_chrome(playwright, request) -> Browser:
    return playwright.chromium.launch(
        headless=True,
        slow_mo=request.config.getoption("slow")
    )


def get_context(browser, request, start) -> BrowserContext:
    """Creates a new browser context based on the specified start type.

    This function is responsible for setting up a new browser context with appropriate
    configurations based on the provided `start` parameter. It handles both local and
    remote context creation.
     Args:
        browser (playwright.sync_api.Browser): The parent browser instance.
        request (pytest.FixtureRequest): The pytest fixture request object.
        start (str): The type of context to create, either 'local' or 'remote'.
    """
    if start == 'local':
        context = browser.new_context(
            no_viewport=True,
            locale=request.config.getoption('l')
        )
        context.set_default_timeout(
            timeout=request.config.getoption('t')
        )
        # context.add_cookies([{'url': 'https://example.com', 'name': 'ab_test', 'value': 'd'}]) add cookies if needed
        return context

    elif start == 'remote':
        context = browser.new_context(
            viewport=request.config.getoption('s'),
            locale=request.config.getoption('l')
        )
        context.set_default_timeout(
            timeout=request.config.getoption('t')
        )
        return context


@pytest.fixture(scope="function")
def return_back(browser):
    browser.go_back()
