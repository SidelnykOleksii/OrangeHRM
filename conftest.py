import pytest
from dotenv import load_dotenv

load_dotenv()

pytest_plugins = [
    'Fixtures.page',
    'Fixtures.user_auth',
    'Fixtures.requests',
    'Fixtures.employees',
    'Fixtures.reporting'
]


def pytest_configure(config):
    env = config.getoption("--env")
    if env == "ci":
        pytest.alluredir = "allure-results"
    else:
        pytest.html = "report.html"
