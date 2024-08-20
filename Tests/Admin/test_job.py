import pytest
from PageObjects.AdminPage.job import JobPage
from PageObjects.default_page import DefaultPageObjects
from Data.utilities import GenerateRandomString


@pytest.mark.usefixtures("user_login")
class TestJob:
    def test_add_new_job_title(self, browser):
        j = JobPage(browser)
        d = DefaultPageObjects(browser)
        job_title = GenerateRandomString.generate_random_str_letters(8)

        d.select_left_side_menu_item("Admin")
        j.add_new_job_titles(job_title, "Some desc", "Some note")
