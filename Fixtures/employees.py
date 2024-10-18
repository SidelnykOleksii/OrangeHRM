import pytest
from PageObjects.PIMPage.add_employee import PimPage
from PageObjects.PIMPage.employee_list import EmployeeList
from PageObjects.default_page import DefaultPageObjects
from Data.utilities import Cookies
from API.PIM.api_employee import APIEmployee


@pytest.fixture(scope="function")
def add_employee(browser):
    p = PimPage(browser)
    d = DefaultPageObjects(browser)

    d.select_left_side_menu_item("PIM")
    p.add_new_employee("First", "Middle", "Last")


@pytest.fixture(scope="function")
def delete_employee(browser):
    e = EmployeeList(browser)
    d = DefaultPageObjects(browser)
    yield
    d.select_left_side_menu_item("PIM")
    e.delete_employee_by_name("First Middle")


@pytest.fixture(scope="function")
def api_add_employee(browser):
    session_cookie = Cookies(browser).get_cookie()
    APIEmployee.api_create_employee(session_cookie=session_cookie)
