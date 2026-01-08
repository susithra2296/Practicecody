from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

def test_view12():
    browser = webdriver.Firefox()

    URL = "https://the-internet.herokuapp.com/drag_and_drop"

    browser.get(URL)

    browser.maximize_window()

    source_element = browser.find_element(By.ID, value="column-a")
    destination_element = browser.find_element(By.ID, value="column-b")
    actions =ActionChains(browser)
    actions.drag_and_drop(source_element,destination_element).perform()