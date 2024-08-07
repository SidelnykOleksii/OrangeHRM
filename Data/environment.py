import os


class Environment:
    SHOT = 'shot'
    PROD = 'prod'

    URLS = {
        SHOT: 'https://example.com/',
        PROD: 'https://opensource-demo.orangehrmlive.com/'
    }

    def __init__(self):
        try:
            self.env = os.getenv('ENV', self.PROD)
        except KeyError:
            raise Exception("ENV variable not found. Please set it correctly.")

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


host = Environment()
