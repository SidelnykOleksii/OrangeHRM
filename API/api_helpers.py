from playwright.sync_api import Page


class Cookies:
    def __init__(self, page: Page):
        self.page = page

    def get_orangehrm_cookie(self):
        cookies = self.page.context.cookies()
        for cookie in cookies:
            if cookie['name'] == 'orangehrm':
                session_cookie_value = cookie['value']
                return session_cookie_value
        return None