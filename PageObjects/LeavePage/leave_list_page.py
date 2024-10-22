from playwright.sync_api import Page
from PageObjects.base import Base
from Utilities.assertions import Assertions


class LeaveListPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    CANCEL_LEAVE_BUTTON = "//div[@class='orangehrm-header-container']//button[text()=' Cancel ']"
    CONFIRM_CANCEL_LEAVE_BUTTON = "//div[@class='orangehrm-modal-footer']//button[text()=' Yes, Confirm ']"

    def assert_leave_exists_in_the_table(self, comments: str):
        self.page.wait_for_load_state('domcontentloaded')
        self.select_sub_page("Leave List")

        row = self.get_table_row_by_value(comments)

        if row == 0:
            raise AssertionError(f"Leave is not found in the table")

    def cancel_leave(self, value: str):
        self.select_row_in_the_table(value)
        self.click(self.CANCEL_LEAVE_BUTTON)
        self.click(self.CONFIRM_CANCEL_LEAVE_BUTTON)