from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


def test_view11():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/nested_frames")
    driver.maximize_window()

    driver.switch_to.frame("frame-top")

    driver.switch_to.frame("frame-middle")
    content= driver.find_element(By.ID, value="content")
    print(f"content {content}")