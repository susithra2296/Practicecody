from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

def test_view1():
    driver = webdriver.Firefox()
    driver.get("https://artoftesting.com/samplesiteforselenium")
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    checkboxs = driver.find_elements(By.XPATH, value=("//input[@type='checkbox']"))
    for checkbox in checkboxs:
        checkbox.send_keys(Keys.SPACE)