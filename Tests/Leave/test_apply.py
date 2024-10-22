import pytest
from PageObjects.LeavePage.apply_page import ApplyLeavePage
from PageObjects.LeavePage.leave_list_page import LeaveListPage
from PageObjects.default_page import DefaultPageObjects


@pytest.mark.usefixtures('user_login')
class TestApplyLeave:
    def test_apply_leave_valid_data(self, browser):
        a = ApplyLeavePage(browser)
        l = LeaveListPage(browser)
        d = DefaultPageObjects(browser)

        d.select_left_side_menu_item("Leave")
        d.select_sub_page("Apply")
        a.apply_leave_with_valid_data(from_date="2024-29-10", comments="some comment")
        l.assert_leave_exists_in_the_table(comments="some comment")
        l.cancel_leave(value="some comment")
