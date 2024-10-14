import pytest
from PageObjects.PIMPage.employee_list import EmployeeList
from PageObjects.default_page import DefaultPageObjects
from API.PIM.api_employee import APIEmployee
from Data.utilities import Cookies


@pytest.mark.usefixtures('user_login')
class TestEmployeeList:
    def test_delete_employee(self, browser):
        e = EmployeeList(browser)
        d = DefaultPageObjects(browser)
        session_cookie = Cookies(browser).get_cookie()
        APIEmployee.api_create_employee(session_cookie=session_cookie)

        d.select_left_side_menu_item("PIM")
        e.delete_employee_by_name("First Middle")
