from dotenv import load_dotenv

load_dotenv()

pytest_plugins = [
    'Fixtures.page',
    'Fixtures.user_auth',
    'Fixtures.requests',
    'Fixtures.employees',
    'Fixtures.reporting'
]


def pytest_addoption(parser):
    """Custom command line options"""
    parser.addoption('--bn', action='store', default="chrome", help="Choose browser: chrome, remote_chrome or firefox")
    parser.addoption('--h', action='store', default=False, help='Choose headless: True or False')
    parser.addoption('--s', action='store', default={'width': 1920, 'height': 1080}, help='Size window: width,height')
    parser.addoption('--slow', action='store', default=200, help='Choose slow_mo for robot action')
    parser.addoption('--t', action='store', default=10000, help='Choose timeout')
    parser.addoption('--l', action='store', default='en_GB', help='Choose locale')
    parser.addoption('--env', action='store', default="local", help="Environment (local or ci)")
