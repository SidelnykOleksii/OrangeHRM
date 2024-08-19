import pytest
import allure
import logging
from PageObjects.default_page import DefaultPageObjects

logging.basicConfig(filename='logging.log', level=logging.INFO)


@pytest.mark.usefixtures('user_login')
class TestDefaultPage:
    @allure.title('User can log out')
    @pytest.mark.smoke
    def test_log_out(self, browser):
        d = DefaultPageObjects(browser)
        d.click_log_out_button()
        d.assertions.check_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", msg="Wrong URL")

    @allure.title('User can search left side menu items using letters')
    def test_search_left_side_menu_items_by_letters(self, browser):
        d = DefaultPageObjects(browser)
        d.left_side_menu_search('d', 3)

    @allure.title('User can not search left side menu items using numbers')
    def test_search_left_side_menu_items_by_numbers(self, browser):
        d = DefaultPageObjects(browser)
        d.left_side_menu_search('8', 0)

    @allure.title('Left side menu items should be 12')
    @pytest.mark.smoke
    def test_default_left_side_menu_items(self, browser):
        d = DefaultPageObjects(browser)
        d.get_default_left_side_menu_items()

    @allure.title('About pop-up titles should be as expected')
    def test_default_titles_in_about_pop_up(self, browser):
        d = DefaultPageObjects(browser)
        d.assert_title_items_in_about_pop_up()

    @allure.title('Header item displayed according to the selected menu')
    def test_header_item_according_to_selected_menu(self, browser):
        d = DefaultPageObjects(browser)
        d.assert_header_item_according_to_selected_menu_item()
