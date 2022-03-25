import pytest

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.fixture(scope="module")
def oneTimeSetUp(browser, osType):
    print("Running one time setUp")
    if browser == 'Chrome':
        print("Runnign test on the Chrome")
    else:
        print("Running test on FF")
    yield
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")