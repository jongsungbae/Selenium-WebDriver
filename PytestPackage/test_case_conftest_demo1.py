import pytest

@pytest.fixture()
def setUp():
    print("Running conftest demo1 setUp")

def test_methodA(setUp):
    print("Running conftest demo1 method A")

def test_methodB(setUp):
    print("Running conftest demo1 method B")

