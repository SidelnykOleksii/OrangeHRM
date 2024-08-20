import allure
from playwright.sync_api import Page, TimeoutError, Response
from Data.environment import host


DROPDOWN = "//nav[@class='oxd-topbar-body-nav']/ul/li//span"
MENU_ITEM = "//ul[@class='oxd-dropdown-menu']/li/a"
SAVE_BUTTON = "//div/button[@type='submit']"

class Base:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def open(self, uri) -> Response | None:
        return self.page.goto(f"{host.get_base_url()}{uri}", wait_until='domcontentloaded')

    @allure.step
    def click(self, locator: str) -> None:
        self.page.click(locator)

    @allure.step
    def input(self, locator: str, data: str) -> None:
        self.page.locator(locator).fill(data)

    def get_items_lists(self, locator: str):
        items = self.page.locator(locator).all_inner_texts()
        i = sorted(items)
        return i

    def select_dropdown_option_by_name(self, dropdown: str, option_text: str):
        dropdown = self.page.locator(DROPDOWN, has_text=dropdown)
        dropdown.click()
        self.page.locator(MENU_ITEM, has_text=option_text).click()

    def click_on_save_button(self):
        self.click(SAVE_BUTTON)

    def upload_file(self, locator: str, file_path: str):
        with self.page.expect_file_chooser() as fc_info:
            self.click(locator)
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
