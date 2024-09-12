import pytest
from PageObjects.AdminPage.user_management import AdminPage
from PageObjects.default_page import DefaultPageObjects
from Data.utilities import GenerateRandomString


@pytest.mark.usefixtures('user_login')
class TestUserManagement:
    def test_add_new_user(self, browser, add_employee):
        a = AdminPage(browser)
        d = DefaultPageObjects(browser)
        username = GenerateRandomString.generate_random_str_letters(8)
        password = GenerateRandomString.generate_random_str_letters_and_digits(10)

        d.select_left_side_menu_item("Admin")
        a.add_new_user(user_role="Admin", employee_name="First Middle Last", username=username, password=password,
                       confirm_pass=password, status="Enabled")
        a.delete_user_by_name(username=username)
