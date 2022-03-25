import pytest

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.fixture(scope="module")
def oneTimeSetUp():
    print("Running one time setUp")
    yield
    print("Running one time tearDown")
