import pytest
from PageObjects.PIMPage.add_employee import PimPage
from PageObjects.PIMPage.employee_list import EmployeeList
from PageObjects.default_page import DefaultPageObjects
from API.PIM.api_employee import APIEmployee


@pytest.mark.usefixtures('user_login')
class TestAddEmployee:
    def test_add_new_employee(self, browser, get_cookies):
        d = DefaultPageObjects(browser)
        p = PimPage(browser)
        e = EmployeeList(browser)

        d.select_left_side_menu_item("PIM")
        p.add_new_employee("First", "Middle", "Last")

        employee_id = e.get_employee_id_from_url()

        d.select_left_side_menu_item("PIM")
        APIEmployee.api_delete_employee_by_id(employee_id, session_cookie=get_cookies)