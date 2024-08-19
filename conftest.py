from dotenv import load_dotenv

load_dotenv()

pytest_plugins = [
    'Fixtures.page',
    'Fixtures.user_auth',
    'Fixtures.requests',
    'Fixtures.employees'
]
