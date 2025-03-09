from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

def test_view12():
    browser = webdriver.Firefox()

    URL = "https://the-internet.herokuapp.com/horizontal_slider"

    browser.get(URL)

    browser.maximize_window()

    slider = browser.find_element(By.XPATH, value="//input[@type ='range']")

    actions = ActionChains(browser)
    actions.click_and_hold(slider).move_by_offset(50,0).release().perform()
