import pytest


@pytest.fixture(scope="session", autouse=True)
def report_path():
    report_dir = "C:/PythonPlaywrightStudy/OrangeHRM/Report"
    report_file = "report.html"
    report_path = f"{report_dir}/{report_file}"
    yield report_path
    print(f"\nReport path: {report_path}")
    print(f"To see trace use command: playwright show-trace ./Tests/trace.zip")