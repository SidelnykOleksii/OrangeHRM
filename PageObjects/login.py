import allure
from playwright.sync_api import Page
from PageObjects.base import Base
from Data.constants import Constants
from Data.assertions import Assertions

USERNAME_FIELD = "//input[@name='username']"
PASSWORD_FIELD = "//input[@name='password']"
SUBMIT_BUTTON = "//button[@type='submit']"
INVALID_CREDENTIALS_ERROR_MESSAGE = "//p[text()[contains(.,'Invalid credentials')]]"


class LoginPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)

    @allure.step
    def user_login(self):
        self.open("web/index.php/auth/login")
        self.input(USERNAME_FIELD, Constants.login)
        self.input(PASSWORD_FIELD, Constants.password)
        self.click(SUBMIT_BUTTON)
        self.assertions.check_URL("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", "Wrong URL")

    @allure.step
    def login_invalid_username(self):
        self.open("web/index.php/auth/login")
        self.input(USERNAME_FIELD, "invalid_username")
        self.input(PASSWORD_FIELD, Constants.password)
        self.click(SUBMIT_BUTTON)
        self.assertions.check_presence(INVALID_CREDENTIALS_ERROR_MESSAGE)

    @allure.step
    def login_invalid_password(self):
        self.open("web/index.php/auth/login")
        self.input(USERNAME_FIELD, Constants.login)
        self.input(PASSWORD_FIELD, "invalid_password")
        self.click(SUBMIT_BUTTON)
        self.assertions.check_presence(INVALID_CREDENTIALS_ERROR_MESSAGE)
