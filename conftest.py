import pytest
@pytest.fixture(autouse=False)
def setup():
    print("launch setup")
    print("login")
    print("browser")
    yield
    print("logoff")
    print("close the browser")

