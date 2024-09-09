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
    INVALID_CREDENTIALS_ERROR_MESSAGE = "//div[contains(@class, 'oxd-alert-content--error')]" \
                                        "//p[text()='Invalid credentials']"
    REQUIRED_ERROR_MESSAGE = "//span[contains(@class, 'input-field-error-message oxd') and text()='Required']"

    @allure.step
    def user_login(self):
        # TODO: think about solution for not use wait_for_timeout.
        self.open("web/index.php/auth/login")
        self.input(self.USERNAME_FIELD, Constants.login)
        self.input(self.PASSWORD_FIELD, Constants.password)
        self.click(self.SUBMIT_BUTTON)
        self.assertions.check_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",
                                  "Wrong URL")
        self.page.wait_for_timeout(timeout=1000)  # temporary solution, without this check test is passed
        # if set expect(loc).to_be_hidden for assert_header_is_visible()
        self.assert_header_is_visible()

    @allure.step
    def login_invalid_data(self, username: str, password: str):
        # TODO: think about solution for not use wait_for_timeout.
        self.open("web/index.php/auth/login")
        self.input(self.USERNAME_FIELD, username)
        self.input(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)
        self.page.wait_for_load_state('domcontentloaded')
        self.page.wait_for_timeout(timeout=1000)  # temporary solution, without this check test is passed
        # if set check_absence
        self.assertions.check_presence(self.INVALID_CREDENTIALS_ERROR_MESSAGE)

    def login_empty_fields(self, username: str, password: str):
        self.open("web/index.php/auth/login")
        self.input(self.USERNAME_FIELD, username)
        self.input(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)
        self.assertions.check_presence(self.REQUIRED_ERROR_MESSAGE)
