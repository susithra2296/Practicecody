import pytest

# class Testmethod:
#     @pytest.fixture(autouse=True, scope="session")
#     def setup(self):
#         print("launch setup")
#         print("login")
#         print("browser")
#         yield
#         print("logoff")
#         print("close the browser")
#
#     def test_add_item(self):
#         print("add the item")
#
#     def test_del_item(self):
#         print("remove item")

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected