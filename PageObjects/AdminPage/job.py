from playwright.sync_api import Page
from PageObjects.base import Base
from Data.assertions import Assertions


# buttons
ADD_JOB_TITLE = "//div[@class='orangehrm-header-container']//button"

# text fields
JOB_TITLE_FIELD = "form > div:nth-child(1) > div > div:nth-child(2) > input"
JOB_DESCRIPTION_FIELD = "form > div:nth-child(2) > div > div:nth-child(2) > textarea"

# other
JOB_SPECIFICATION_INPUT = "//div[@class='oxd-file-input-div']"


class JobPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)

    def add_new_job_titles(self, job_title: str, job_desc: str, note: str):
        self.select_dropdown_option_by_name(dropdown="Job ", option_text="Job Titles")
        self.page.locator(ADD_JOB_TITLE).click()
        self.input(JOB_TITLE_FIELD, job_title)
        self.input(JOB_DESCRIPTION_FIELD, job_desc)

        # need to investigate upload, task created in Trello
        # self.upload_file(locator=JOB_SPECIFICATION_INPUT, file_path="TestData/UploadFiles/UploadFileValid.txt")
        # text = self.page.locator(JOB_SPECIFICATION_INPUT, has_text="No file chosen")
        # text.is_hidden(timeout=300)

        add_note_loc = self.page.get_by_placeholder(text="Add note")
        add_note_loc.fill(note)
        self.click_on_save_button()
        self.assertions.check_url(uri="https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList",
                                  msg="Wrong url")
