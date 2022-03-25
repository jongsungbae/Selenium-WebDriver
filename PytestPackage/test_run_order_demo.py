import pytest

@pytest.mark.run(order=2)
def test_run_order_methodA(oneTimeSetUp, setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print("Running method B")

def test_run_order_methodC(oneTimeSetUp, setUp):
    print("Running method C")

def test_run_order_methodD(oneTimeSetUp, setUp):
    print("Running method D")

def test_run_order_methodE(oneTimeSetUp, setUp):
    print("Running method E")

def test_run_order_methodF(oneTimeSetUp, setUp):
    print("Running method F")

