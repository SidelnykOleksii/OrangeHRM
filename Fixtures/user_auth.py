import pytest
from PageObjects.login import LoginPage
from PageObjects.default_page import DefaultPageObjects
from API.api_helpers import Cookies


@pytest.fixture(scope='function')
def user_login(browser):
    l = LoginPage(browser)
    l.user_login()


@pytest.fixture(scope='function', autouse=True)
def log_out(browser):
    d = DefaultPageObjects(browser)
    d.log_out()


@pytest.fixture(scope='function')
def get_cookies(browser):
    c = Cookies(browser)
    cookie = c.get_orangehrm_cookie()
    return cookie

