import pytest

@pytest.fixture()
def setUp():
    print("Running conftest setUp")
    yield
    print("Running conftest tearDown")

@pytest.fixture(scope="module")
def ontTimeSetUp():
    print("Running conftest on time setUp")
    yield
    print("Running conftest on time tearDown")
