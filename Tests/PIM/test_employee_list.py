import pytest
from PageObjects.PIMPage.employee_list import EmployeeList
from PageObjects.default_page import DefaultPageObjects


@pytest.mark.usefixtures('user_login')
class TestEmployeeList:
    def test_delete_employee(self, browser, api_add_employee):
        e = EmployeeList(browser)
        d = DefaultPageObjects(browser)

        d.select_left_side_menu_item("PIM")
        e.delete_employee_by_name("First Middle")
