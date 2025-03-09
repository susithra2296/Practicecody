from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


def test_view1():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    time.sleep(2)
    driver.maximize_window()
    dd_element=driver.find_element(By.ID,value="dropdown")
    select=Select(dd_element)
    option_count=len(select.options)

    experted_count = 3
    if option_count == experted_count:
        print("count is correct")
    else:
        print("count is incorrect")
    # select.select_by_index("2")
    # select.select_by_value(2)
    # select.select_by_visible_text("Option 2")

