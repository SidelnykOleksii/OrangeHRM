import allure
import pytest

from PageObjects.login import LoginPage


class TestLogin:
    @allure.title('User can log in with valid data')
    @pytest.mark.smoke
    def test_user_valid_login(self, browser):
        l = LoginPage(browser)
        l.user_login()

    @allure.title('User can not log in with invalid username')
    def test_login_invalid_username(self, browser):
        l = LoginPage(browser)
        l.login_invalid_username()

    @allure.title('User can not log in with invalid password')
    def test_login_invalid_password(self, browser):
        l = LoginPage(browser)
        l.login_invalid_password()
