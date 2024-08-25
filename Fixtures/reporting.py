import pytest


@pytest.fixture(scope="session", autouse=True)
def shows_trace():
    print(f"\nTo see trace use command: playwright show-trace trace.zip")