
class PathToTestFiles:
    @staticmethod
    def upload_file_valid():
        file_path = "C:/PythonPlaywrightStudy/OrangeHRM/TestData/UploadFiles/UploadFileValid.txt"
        return file_path


class PageUrls:
    @staticmethod
    def page_urls():
        page_urls = {
            'view_job_tile_list_page': 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList',
            'view_system_users_page': 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
            }
        return page_urls
