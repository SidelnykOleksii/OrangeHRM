import allure
import pytest
from pytest import mark
from PageObjects.login import LoginPage
from Data.constants import Constants


missed_required_filed = {
    "argnames": 'login, password',
    "argvalues": [('', 'admin123'),
                  ('Admin', '')],
    "ids": ['missed login', 'missed password']
}


class TestLogin:
    @allure.title('User can log in with valid data')
    @pytest.mark.smoke
    def test_user_valid_login(self, browser):
        l = LoginPage(browser)
        l.user_login()

    @mark.parametrize(**missed_required_filed)
    def test_required_fields(self, browser, login, password):
        l = LoginPage(browser)
        l.login_empty_fields(login, password)

    @allure.title('User can not log in with invalid username')
    def test_login_invalid_username(self, browser):
        l = LoginPage(browser)
        l.login_invalid_data("invalidname", Constants.password)

    @allure.title('User can not log in with invalid password')
    def test_login_invalid_password(self, browser):
        l = LoginPage(browser)
        l.login_invalid_data(Constants.login, "invalidpass")
