import pytest


@pytest.fixture(scope="session", autouse=True)
def shows_trace(request):
    if request.config.getoption("bn") != 'remote_chrome':
        print(f"\nTo see trace use command: playwright show-trace trace.zip")