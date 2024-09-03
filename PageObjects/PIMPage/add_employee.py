from playwright.sync_api import Page
from PageObjects.base import Base
from Data.assertions import Assertions


class PimPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)

    # locators
    # text fields
    ADD_EMPLOYEE_FIRST_NAME = "//div/input[@name='firstName']"
    ADD_EMPLOYEE_MIDDLE_NAME = "//div/input[@name='middleName']"
    ADD_EMPLOYEE_LAST_NAME = "//div/input[@name='lastName']"

    # buttons
    ADD_EMPLOYEE_BUTTON = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    ADD_EMPLOYEE_SAVE_BUTTON = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

    # other
    EDIT_EMPLOYEE_IMAGE = "//div[@class='orangehrm-edit-employee-image']"

    def add_new_employee(self, first_name: str, middle_name: str, last_name: str):
        self.click(self.ADD_EMPLOYEE_BUTTON)
        self.input(self.ADD_EMPLOYEE_FIRST_NAME, first_name)
        self.input(self.ADD_EMPLOYEE_MIDDLE_NAME, middle_name)
        self.input(self.ADD_EMPLOYEE_LAST_NAME, last_name)
        self.click(self.ADD_EMPLOYEE_SAVE_BUTTON)
        self.assertions.check_presence(self.EDIT_EMPLOYEE_IMAGE)
