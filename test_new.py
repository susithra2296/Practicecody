import pytest
import math

@pytest.mark.skip
def testlogin():
    print("login sucess")

@pytest.mark.sanity
def testfail():
    print("login fail")

@pytest.mark.xfail
def test_calcultaion():
    assert 1+1 == 5

def test_squre():
    num = 25
    assert math.sqrt(num) == 5

def test_squre1():
    num = 25
    assert num < 5




