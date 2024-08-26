import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


@pytest.fixture(scope='class')
def browser(request) -> Page:
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
        # context.add_cookies([{'url': 'https://example.ru', 'name': 'ab_test', 'value': 'd'}]) add cookies if needed
        return context


@pytest.fixture(scope="function")
def return_back(browser):
    browser.go_back()


# @pytest.fixture(scope="function")
# def console_message(browser, page: Page):
#     page.on("console", lambda msg: print(f"error: {msg.text}") if msg.type == "error" else None)
#     yield page
