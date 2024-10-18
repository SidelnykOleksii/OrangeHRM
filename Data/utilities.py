import random
import string
from playwright.sync_api import Page


class GenerateRandomString:
    @staticmethod
    def generate_random_str_letters(length: int):
        s = ''.join(random.choices(string.ascii_letters, k=length))
        return s

    @staticmethod
    def generate_random_str_letters_and_digits(length: int):
        digit = random.choice(string.digits)
        s = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        result = list(s + digit)
        random.shuffle(result)
        return ''.join(result)


class Cookies:
    def __init__(self, page: Page):
        self.page = page

    def get_cookie(self):
        cookies = self.page.context.cookies()
        for cookie in cookies:
            if cookie['name'] == 'orangehrm':
                session_cookie_value = cookie['value']
                return session_cookie_value
        return None
