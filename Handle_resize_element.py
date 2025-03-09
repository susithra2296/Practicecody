from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

def test_view11():
    driver = webdriver.Firefox()
    driver.get("https://demo.automationtesting.in/Resizable.html")
    driver.maximize_window()
    time.sleep(2)
    resize_element = driver.find_element(By.XPATH, value="//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
    initial_size = driver.find_element(By.XPATH, value="//div[@id='resizable']")
    initial_size_value = initial_size.size
    print(f"initial_size_value{initial_size_value}")

    actions = ActionChains(driver)
    actions.click_and_hold(resize_element).move_by_offset(100,100).release().perform()

    resize_element = initial_size.size
    print(f"{resize_element}")
