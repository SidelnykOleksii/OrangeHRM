import pytest
from PageObjects.login import LoginPage
from PageObjects.default_page import DefaultPageObjects


@pytest.fixture(scope='function')
def user_login(browser):
    l = LoginPage(browser)
    l.user_login()


@pytest.fixture(scope='function', autouse=True)
def log_out(browser):
    d = DefaultPageObjects(browser)
    d.log_out()
