from playwright.sync_api import Page, expect
from PageObjects.base import Base
from Data.assertions import Assertions
from Data.variables import PageUrls


class AdminPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)

    # locators
    # buttons
    ADD_USER_BUTTON = "//div[@class='orangehrm-header-container']/button"
    SAVE_NEW_USER_BUTTON = "//button[text()[contains(.,'Save')]]"

    # fields
    USERNAME_FIELD = "//label[text()='Username']/ancestor::div[contains(@class, 'input-field')]//input"
    PASSWORD_FIELD = "//label[text()='Password']/ancestor::div[contains(@class, 'input-field')]//input"
    CONFIRM_PASSWORD_FIELD = "//label[text()='Confirm Password']/ancestor::div[contains(@class, 'input-field')]//input"

    # table
    TABLE_BODY = "//div[@class='oxd-table-body']"
    TABLE_NAME_CELL = "//div[text()='{}']"

    def select_user_role(self, user_role: str):
        self.page.get_by_text("-- Select --").first.click()
        self.page.get_by_role("option", name=user_role).locator("span").click()

    def select_employee(self, employee_name: str):
        self.page.get_by_placeholder("Type for hints...").click()
        self.page.get_by_placeholder("Type for hints...").fill(employee_name)
        self.page.get_by_text(employee_name).first.click()

    def input_username(self, username: str):
        self.input(self.USERNAME_FIELD, username)

    def select_status(self, status: str):
        self.page.get_by_text("-- Select --").click()
        self.page.get_by_text(status).click()

    def set_pass(self, password: str):
        self.input(self.PASSWORD_FIELD, password)

    def confirm_pass(self, confirm_pass: str):
        self.input(self.CONFIRM_PASSWORD_FIELD, confirm_pass)

    def delete_user_by_name(self, username: str):
        self.page.wait_for_load_state("domcontentloaded")
        rows = self.page.locator(self.TABLE_BODY)
        for i in range(rows.count()):
            row = rows.nth(i)
            row_by_name = row.locator(f"{self.TABLE_NAME_CELL.format(username)}"
                                      f"/ancestor::div[contains(@class, 'oxd-table-row')]")
            try:
                delete_button = row_by_name.locator("//i[@class='oxd-icon bi-trash']")
                delete_button.click()
                self.page.get_by_role("button", name=" Yes, Delete").click()
                self.page.wait_for_load_state("domcontentloaded")

                expect(row_by_name).not_to_be_visible()
                return
            except Exception as e:
                print(f"Error finding user {username}: {e}")

        raise AssertionError(f"User {username} still exists in the table")

    def assert_user_exists_in_the_table(self, username: str):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(timeout=1000)
        rows = self.page.locator(self.TABLE_BODY)

        for i in range(rows.count()):
            row = rows.nth(i)
            name_locator = row.locator(self.TABLE_NAME_CELL.format(username))
            try:
                expect(name_locator).to_have_count(1)
                expect(name_locator).to_be_visible()
                return
            except Exception as e:
                print(f"Error finding user {username}: {e}")

        raise AssertionError(f"User {username} not found")

    def add_new_user(self, user_role, employee_name, username, password, confirm_pass, status):
        self.click(self.ADD_USER_BUTTON)
        self.select_user_role(user_role)
        self.select_employee(employee_name)
        self.input_username(username)
        self.select_status(status)
        self.set_pass(password)
        self.confirm_pass(confirm_pass)
        self.click(self.SAVE_NEW_USER_BUTTON)
        self.assertions.check_url(uri=PageUrls.page_urls()["view_system_users_page"],
                                  msg="Wrong URL")
        self.assert_user_exists_in_the_table(username)
