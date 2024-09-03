from playwright.sync_api import Page
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
    USERNAME_FIELD = "div > div:nth-child(4) > div > div:nth-child(2) > input"
    PASSWORD_FIELD = "div > div.oxd-grid-item.oxd-grid-item--gutters.user-password-cell > div > div:nth-child(2) > input"
    CONFIRM_PASSWORD_FIELD = "div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > div:nth-child(2) > input"

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

    def delete_user_by_name(self, name: str):  # doesn't work correctly, need to check the locators
        self.page.wait_for_selector("//div[@class='oxd-table-card']")
        try:
            rows = self.page.locator("//div[@class='oxd-table-row oxd-table-row--with-border']").all()
            for row in rows:
                if row.text_content() == name:
                    delete_button = row.locator("//i[@class='oxd-icon bi-trash']")
                    delete_button.click()
                    self.page.get_by_role("button", name=" Yes, Delete").click()
                    break
            else:
                print(f"Row with '{name}' is not found")
        except Exception as e:
            print(f"An error occurred: {e}")

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
        # need to add a check for displaying the user in the list
