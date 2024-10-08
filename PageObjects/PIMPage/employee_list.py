import re

from playwright.sync_api import Page, expect
from PageObjects.base import Base
from Data.assertions import Assertions


class EmployeeList(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    # locators
    # employee table
    EMPLOYEE_TABLE = "//div[contains(@class, 'orangehrm-employee-list')]"

    def delete_employee_by_name(self, employee_name: str):
        self.page.wait_for_load_state("domcontentloaded")
        self.assertions.check_presence(self.EMPLOYEE_TABLE)
        row_by_name = self.get_table_row_by_name(employee_name)

        try:
            row_by_name.locator(self.DELETE_BUTTON).click()
            self.page.locator(self.CONFIRM_DELETE_BUTTON).click()

            expect(row_by_name).not_to_be_visible()
        except Exception as e:
            raise Exception(f"Error deleting employee{employee_name}: {e}")

    def get_employee_id_from_url(self):
        # edit employee form should be opened
        self.page.wait_for_load_state("domcontentloaded")
        current_url = self.page.url
        match = re.search(r'empNumber/(\d+)', current_url)
        if match:
            return match.group(1)
        else:
            raise ValueError("Employee ID not found in the URL")
