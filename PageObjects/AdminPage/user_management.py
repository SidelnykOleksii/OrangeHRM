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

    # dropdowns
    SHOW_DROPDOWN_OPTIONS = "//label[text()='{}']/ancestor::" \
                            "div[contains(@class, 'input-field-bottom-space')]//div/i"

    # table
    TABLE_BODY = "//div[@class='oxd-table-body']"
    TABLE_CELL = "//div[text()='{}']"
    EDIT_BUTTON = "//div[@class='oxd-table-cell-actions']/button/i[@class='oxd-icon bi-pencil-fill']"
    DELETE_BUTTON = "//div[@class='oxd-table-cell-actions']/button/i[@class='oxd-icon bi-trash']"

    # confirm delete modal
    CONFIRM_DELETE_BUTTON = "//div[@class='orangehrm-modal-footer']//button[text()=' Yes, Delete ']"
    CANCEL_DELETE_BUTTON = "//div[@class='orangehrm-modal-footer']/button[text()=' No, Cancel ']"

    # edit user form
    EDIT_USER_FORM = "//div[@class='orangehrm-card-container']/h6[text()='Edit User']"

    def select_user_role(self, user_role: str):
        self.page.locator(self.SHOW_DROPDOWN_OPTIONS.format("User Role")).click()
        self.page.get_by_role("option", name=user_role).locator("span").click()

    def select_employee(self, employee_name: str):
        self.page.get_by_placeholder("Type for hints...").click()
        self.page.get_by_placeholder("Type for hints...").fill(employee_name)
        self.page.get_by_text(employee_name).first.click()

    def input_username(self, username: str):
        self.input(self.USERNAME_FIELD, username)

    def select_status(self, status: str):
        self.page.locator(self.SHOW_DROPDOWN_OPTIONS.format("Status")).click()
        self.page.get_by_text(status).click()

    def set_pass(self, password: str):
        self.input(self.PASSWORD_FIELD, password)

    def confirm_pass(self, confirm_pass: str):
        self.input(self.CONFIRM_PASSWORD_FIELD, confirm_pass)

    def delete_user_by_name(self, username: str):
        self.page.wait_for_load_state("domcontentloaded")
        row_by_name = self.page.locator(f"{self.TABLE_CELL.format(username)}"
                                        f"/ancestor::div[contains(@class, 'oxd-table-row')]")
        try:
            row_by_name.locator(self.DELETE_BUTTON).click()
            self.page.locator(self.CONFIRM_DELETE_BUTTON).click()
            self.page.wait_for_load_state("domcontentloaded")

            expect(row_by_name).not_to_be_visible()
        except Exception as e:
            raise Exception(f"User {username} still exists in the table") from {e}

    def assert_user_exists_in_the_table(self, username: str):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(timeout=2000)  # temporary solution
        name_locator = self.page.locator(self.TABLE_CELL.format(username))

        try:
            expect(name_locator).to_have_count(1)
            expect(name_locator).to_be_visible()
        except Exception as e:
            raise AssertionError(f"Error finding user {username}: {e}")

    def verify_user_data_in_the_table(self, username, user_role, status, employee):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(timeout=2000)  # temporary solution

        row_by_username = self.page.locator(f"{self.TABLE_CELL.format(username)}"
                                            f"/ancestor::div[contains(@class, 'table-row--with-border')]")

        if row_by_username == 0:
            raise AssertionError(f"User {username} is not found in the table")

        user_role_locator = row_by_username.locator("div:nth-child(3)")
        status_locator = row_by_username.locator("div:nth-child(5)")
        employee_locator = row_by_username.locator("div:nth-child(4)")

        try:
            expect(row_by_username).to_be_visible()
            expect(user_role_locator).to_have_text(user_role)
            expect(status_locator).to_have_text(status)
            expect(employee_locator).to_have_text(employee)

        except Exception as e:
            raise AssertionError(f"Verification failed for user {username}: {e}")

    def add_new_user(self, user_role, employee_name, username, password, confirm_pass, status):
        self.click(self.ADD_USER_BUTTON)
        self.select_user_role(user_role)
        self.select_employee(employee_name)
        self.input_username(username)
        self.select_status(status)
        self.set_pass(password)
        self.confirm_pass(confirm_pass)
        self.click(self.SAVE_NEW_USER_BUTTON)
        self.assert_user_exists_in_the_table(username)

    def open_edit_user_form(self, username):
        self.page.wait_for_load_state("domcontentloaded")
        row_by_name = self.page.locator(f"{self.TABLE_CELL.format(username)}"
                                        f"/ancestor::div[contains(@class, 'oxd-table-row')]")
        try:
            row_by_name.locator(self.EDIT_BUTTON).click()
            self.page.locator(self.EDIT_USER_FORM).is_visible()

        except Exception as e:
            raise Exception(f"User not found. Error: {e}")

    def edit_required_user_data(self, user_role, status, edited_username, employee=None):
        self.select_user_role(user_role)

        if employee is None:
            pass
        else:
            self.select_employee(employee)

        self.select_status(status)
        self.input_username(edited_username)
        self.click_on_save_button()
