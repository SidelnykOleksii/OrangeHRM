import allure
from playwright.sync_api import Page
from PageObjects.base import Base
from Data.constants import Constants
from Data.assertions import Assertions


class LoginPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)

    # locators
    USERNAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    INVALID_CREDENTIALS_ERROR_MESSAGE = "//p[text()[contains(.,'Invalid credentials')]]"
    REQUIRED_ERROR_MESSAGE = "//div/span[@class='oxd-text oxd-text--span oxd-input-field-error-message" \
                             " oxd-input-group__message']"

    @allure.step
    def user_login(self):
        self.open("web/index.php/auth/login")
        self.input(self.USERNAME_FIELD, Constants.login)
        self.input(self.PASSWORD_FIELD, Constants.password)
        self.click(self.SUBMIT_BUTTON)
        self.assertions.check_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",
                                  "Wrong URL")
        self.assert_header_is_visible()

    @allure.step
    def login_invalid_data(self, username: str, password: str):
        self.open("web/index.php/auth/login")
        self.input(self.USERNAME_FIELD, username)
        self.input(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)
        self.assertions.check_presence(self.INVALID_CREDENTIALS_ERROR_MESSAGE)

    def login_empty_fields(self, username: str, password: str):
        self.open("web/index.php/auth/login")
        self.input(self.USERNAME_FIELD, username)
        self.input(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)
        self.assertions.check_presence(self.REQUIRED_ERROR_MESSAGE)