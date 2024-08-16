import pytest
from PageObjects.AdminPage.user_management import AdminPage
from PageObjects.default_page import DefaultPageObjects


@pytest.mark.usefixtures('user_login')
class TestUserManagement:
    def test_add_new_user(self, browser):
        a = AdminPage(browser)
        d = DefaultPageObjects(browser)

        d.select_left_side_menu_item("Admin")
        a.add_new_admin(user_role="Admin", employee_name="Qwerty LName", username="Test_Olek3", password="1234567w",
                        confirm_pass="1234567w")