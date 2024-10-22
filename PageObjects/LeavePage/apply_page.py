from playwright.sync_api import Page
from PageObjects.base import Base
from Utilities.assertions import Assertions


class ApplyLeavePage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    # locators
    COMMENTS_FIELD = "//label[text()='Comments']/ancestor::div[contains(@class, 'input-field')]//textarea"
    FROM_DATE_FIELD = "//label[text()='From Date']/ancestor::div[contains(@class, 'input-field')]//input"
    TO_DATE_FIELD = "//label[text()='To Date']/ancestor::div[contains(@class, 'input-field')]//input"

    def select_leave_type(self):
        self.page.locator(self.SHOW_DROPDOWN_OPTIONS.format("Leave Type")).click()
        self.page.get_by_text("CAN - FMLA").click()

    def input_from_date(self, from_date: str):
        self.input(self.FROM_DATE_FIELD, from_date)

    def input_to_date(self, to_date: str):
        self.input(self.TO_DATE_FIELD, to_date)

    def input_comments(self, comments: str):
        self.input(self.COMMENTS_FIELD, comments)

    def apply_leave_with_valid_data(self, from_date: str, comments: str):
        self.page.wait_for_load_state('domcontentloaded')
        self.select_leave_type()
        self.input_from_date(from_date)
        self.input_comments(comments)
        self.click(self.APPLY_BUTTON)
