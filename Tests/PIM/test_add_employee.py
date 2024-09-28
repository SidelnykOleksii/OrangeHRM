import pytest
from PageObjects.PIMPage.add_employee import PimPage
from PageObjects.default_page import DefaultPageObjects


@pytest.mark.usefixtures('user_login')
class TestAddEmployee:
    def test_add_new_employee(self, browser, delete_employee):
        self.d = DefaultPageObjects(browser)
        self.p = PimPage(browser)

        self.d.select_left_side_menu_item("PIM")
        self.p.add_new_employee("First", "Middle", "Last")