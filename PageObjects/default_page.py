import allure
from playwright.sync_api import Page
from PageObjects.base import Base
from Data.assertions import Assertions
import logging


class DefaultPageObjects(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    # locators
    # user details header
    USER_DETAILS_DROPDOWN = '//span[@class="oxd-userdropdown-tab"]'
    USER_DETAILS_DROPDOWN_MENU = '//ul[@class="oxd-dropdown-menu"]'
    HEADER_LEFT_SIDE_TEXT = "//div[@class='oxd-topbar-header']//span/h6"

    # Left side menu
    LEFT_SIDE_MENU_SEARCH_FIELD = "//input[@placeholder='Search']"
    LEFT_SIDE_MENU_ITEMS = "//ul[@class='oxd-main-menu']/li"
    LEFT_SIDE_MENU_ITEM = "//ul[@class='oxd-main-menu']/li//span"

    # About pop-up
    ABOUT_POP_UP = '//div[contains(@class, "shadow oxd-dialog-sheet--gutters")]'
    ABOUT_POP_UP_TITLE_ITEMS = '//div//p[@class="oxd-text oxd-text--p orangehrm-about-title"]'
    ABOUT_POP_UP_CLOSE_BUTTON = "//button[contains(@class, 'oxd-dialog-close-button-position')]"

    about_pop_up_expected_items = ['Company Name:', 'Version:', 'Active Employees:', 'Employees Terminated:']

    @allure.step
    def click_log_out_button(self):
        self.click(self.USER_DETAILS_DROPDOWN)
        self.page.get_by_role("menuitem", name="Logout").click()

    def click_about_button(self):
        self.click(self.USER_DETAILS_DROPDOWN)
        self.page.wait_for_selector(self.USER_DETAILS_DROPDOWN_MENU)
        self.page.get_by_role("menuitem", name="About").click()

    def left_side_menu_search(self, input_value: str, expected_count: int):
        self.page.wait_for_load_state('load')
        self.input(self.LEFT_SIDE_MENU_SEARCH_FIELD, input_value)
        actual_count = self.page.locator(self.LEFT_SIDE_MENU_ITEMS).count()
        assert actual_count == expected_count

    def assert_default_left_side_menu_items(self):
        self.page.wait_for_selector(self.LEFT_SIDE_MENU_ITEMS)
        count = self.page.locator(self.LEFT_SIDE_MENU_ITEMS).count()
        assert count == 12

    def select_left_side_menu_item(self, item_name: str):
        self.page.wait_for_selector(self.LEFT_SIDE_MENU_ITEMS)
        self.page.get_by_role("link", name=item_name).click()

    def log_out(self):
        if self.page.is_visible(self.USER_DETAILS_DROPDOWN):
            self.click_log_out_button()
        else:
            pass

    @allure.step
    def assert_title_items_in_about_pop_up(self):
        expected = sorted(self.about_pop_up_expected_items)
        self.click_about_button()
        self.page.wait_for_selector(self.ABOUT_POP_UP_TITLE_ITEMS)
        actual = self.get_items_lists(self.ABOUT_POP_UP_TITLE_ITEMS)
        self.logger.info(f"Expected items: {expected}")
        self.logger.info(f"Actual items: {actual}")
        for item in expected:
            assert item in actual, f"Item '{item}' is missing in the actual list of items"
            self.logger.info(f"Item '{item}' is present in the actual list of items")
        self.page.locator(self.ABOUT_POP_UP_CLOSE_BUTTON).click()

    def assert_header_item_according_to_selected_menu_item(self):
        menu_items = [
            ("Leave", "Leave"),
            ("Directory", "Directory"),
        ]
        for menu_text, expected_header_text in menu_items:
            self.page.locator(self.LEFT_SIDE_MENU_ITEMS, has_text=menu_text).click()
            actual_header_text = self.page.locator(self.HEADER_LEFT_SIDE_TEXT).inner_text()
            assert actual_header_text == expected_header_text
