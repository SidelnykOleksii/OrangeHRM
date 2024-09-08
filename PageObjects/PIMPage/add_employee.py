from playwright.sync_api import Page
from PageObjects.base import Base
from Data.assertions import Assertions

# text fields
ADD_EMPLOYEE_FIRST_NAME = "//div/input[@name='firstName']"
ADD_EMPLOYEE_MIDDLE_NAME = "//div/input[@name='middleName']"
ADD_EMPLOYEE_LAST_NAME = "//div/input[@name='lastName']"

# buttons
ADD_EMPLOYEE_BUTTON = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
ADD_EMPLOYEE_SAVE_BUTTON = "//button[contains(@class, 'oxd-button--secondary orangehrm-left-space')]"

# other
EDIT_EMPLOYEE_IMAGE = "//div[@class='orangehrm-edit-employee-image']"


class PimPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)

    def add_new_employee(self, first_name: str, middle_name: str, last_name: str):
        self.click(ADD_EMPLOYEE_BUTTON)
        self.input(ADD_EMPLOYEE_FIRST_NAME, first_name)
        self.input(ADD_EMPLOYEE_MIDDLE_NAME, middle_name)
        self.input(ADD_EMPLOYEE_LAST_NAME, last_name)
        self.click(ADD_EMPLOYEE_SAVE_BUTTON)
        self.assertions.check_presence(EDIT_EMPLOYEE_IMAGE)
