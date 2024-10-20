import pytest
from PageObjects.AdminPage.user_management import AdminPage
from PageObjects.default_page import DefaultPageObjects
from Utilities.helpers import GenerateRandomString


@pytest.fixture(scope="function")
def add_user(browser, api_add_employee):
    a = AdminPage(browser)
    d = DefaultPageObjects(browser)
    username = GenerateRandomString.generate_random_str_letters(8)
    password = GenerateRandomString.generate_random_str_letters_and_digits(10)

    d.select_left_side_menu_item("Admin")
    a.add_new_user(user_role="Admin", employee_name="First Middle Last", username=username, password=password,
                   confirm_password=password, status="Enabled")
    return username