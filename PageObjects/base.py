from __future__ import annotations

import allure
from playwright.sync_api import Page, Response, expect
from Data.environment import host


class Base:
    """
    A base class that provides common actions for interacting with web elements using the Playwright library.
    Attributes: page (Page): The Playwright page instance for browser interaction.
    """
    def __init__(self, page: Page):
        self.page = page

    # locators
    HEADER = "//header[@class='oxd-topbar']"
    DROPDOWN = "//nav[@class='oxd-topbar-body-nav']/ul/li//span"
    MENU_ITEM = "//ul[@class='oxd-dropdown-menu']/li/a"
    SAVE_BUTTON = "//div/button[@type='submit']"

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
        dropdown = self.page.locator(self.DROPDOWN, has_text=dropdown)
        dropdown.click()
        self.page.locator(self.MENU_ITEM, has_text=option_text).click()

    def click_on_save_button(self):
        self.click(self.SAVE_BUTTON)

    def upload_file(self, locator: str, file_path: str):
        with self.page.expect_file_chooser() as fc_info:
            self.click(locator)
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def assert_header_is_visible(self):
        self.page.wait_for_load_state('domcontentloaded', timeout=5000)
        loc = self.page.locator(self.HEADER)
        expect(loc).to_be_visible(timeout=5000)
