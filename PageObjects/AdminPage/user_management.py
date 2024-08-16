from playwright.sync_api import Page
from PageObjects.default_page import DefaultPageObjects
from PageObjects.base import Base


ADD_USER_BUTTON = "//div[@class='orangehrm-header-container']/button"


class AdminPage(Base):
    def __int__(self, page: Page) -> None:
        super().__int__(page)
        self.default_page = DefaultPageObjects(page)

    def select_user_role(self, user_role: str):
        self.page.get_by_text("-- Select --").first.click()
        self.page.get_by_role("option", name=user_role).locator("span").click()

    def select_employee(self, employee_name: str):
        self.page.get_by_placeholder("Type for hints...").click()
        self.page.get_by_placeholder("Type for hints...").fill(employee_name)
        self.page.get_by_text(employee_name).click()

    def input_username(self, username: str):
        self.page.get_by_role("textbox").nth(2).click()
        self.page.get_by_role("textbox").nth(2).fill(username)

    def set_pass(self, password: str):
        self.page.get_by_role("textbox").nth(3).click()
        self.page.get_by_role("textbox").nth(3).fill(password)

    def confirm_pass(self, confirm_pass: str):
        self.page.get_by_role("textbox").nth(4).click()
        self.page.get_by_role("textbox").nth(4).fill(confirm_pass)

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

    def add_new_admin(self, user_role, employee_name, username, password, confirm_pass):
        self.page.locator(ADD_USER_BUTTON).click()
        self.select_user_role(user_role)
        self.select_employee(employee_name)
        self.input_username(username)
        self.set_pass(password)
        self.confirm_pass(confirm_pass)
        self.page.get_by_text("-- Select --").click()
        self.page.get_by_text("Enabled").click()
        self.page.get_by_role("button", name="Save").click()
