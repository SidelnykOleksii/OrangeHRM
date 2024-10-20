from playwright.sync_api import Page, expect
from PageObjects.base import Base
from Utilities.assertions import Assertions
from Utilities.variables import PathToTestFiles, PageUrls


class JobPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)

    # locators
    # buttons
    ADD_JOB_TITLE = "//div[@class='orangehrm-header-container']//button"

    # text fields
    JOB_TITLE_FIELD = "//label[text()='Job Title']/ancestor::div[contains(@class, 'input-field-bottom-space')]//input"
    JOB_DESCRIPTION_FIELD = "//label[text()='Job Description']/ancestor::" \
                            "div[contains(@class, 'input-field-bottom-space')]//textarea"

    # other
    JOB_SPECIFICATION_INPUT = "//div[@class='oxd-file-input-div']"

    def add_new_job_titles(self, job_title: str, job_desc: str, note: str, file_name: str):
        self.select_dropdown_option_by_name(dropdown="Job ", option_text="Job Titles")
        self.page.locator(self.ADD_JOB_TITLE).click()
        self.input(self.JOB_TITLE_FIELD, job_title)
        self.input(self.JOB_DESCRIPTION_FIELD, job_desc)
        self.upload_file(locator=self.JOB_SPECIFICATION_INPUT, file_path=PathToTestFiles.upload_file_valid())
        loc = self.page.locator(self.JOB_SPECIFICATION_INPUT)
        expect(loc).to_have_text(file_name)
        add_note_loc = self.page.get_by_placeholder(text="Add note")
        add_note_loc.fill(note)
        self.click_on_save_button()
        self.assertions.check_url(uri=PageUrls.page_urls()["view_job_tile_list_page"],
                                  msg="Wrong url")
