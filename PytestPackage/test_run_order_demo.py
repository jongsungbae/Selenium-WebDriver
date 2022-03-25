import pytest

@pytest.mark.run(order=2)
def test_run_order_methodA(ontTimeSetUp, setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodB(ontTimeSetUp, setUp):
    print("Running method B")

def test_run_order_methodC(ontTimeSetUp, setUp):
    print("Running method C")

def test_run_order_methodD(ontTimeSetUp, setUp):
    print("Running method D")

def test_run_order_methodE(ontTimeSetUp, setUp):
    print("Running method E")

def test_run_order_methodF(ontTimeSetUp, setUp):
    print("Running method F")

