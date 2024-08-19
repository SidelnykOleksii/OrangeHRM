import pytest
from PageObjects.PIMPage.add_employee import PimPage
from PageObjects.default_page import DefaultPageObjects


@pytest.fixture(scope="function")
def add_employee(browser):
    p = PimPage(browser)
    d = DefaultPageObjects(browser)

    d.select_left_side_menu_item("PIM")
    p.add_new_employee("First", "Middle", "Last")
