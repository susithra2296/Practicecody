from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

def test_view11():
    driver = webdriver.Firefox()
    driver.get("https://demo.automationtesting.in/Register.html")
    action = ActionChains(driver)
    mouse_move= driver.find_element(By.XPATH,value="//a[normalize-space()='SwitchTo']")
    action.move_to_element(mouse_move).perform()
    driver.find_element(By.XPATH, value="//a[normalize-space()='Frames']").click()
