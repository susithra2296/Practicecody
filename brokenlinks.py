

import requests
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

def test_view1():
    driver = webdriver.Firefox()
    driver.get("https://jqueryui.com/demos/")
    time.sleep(1)
    driver.maximize_window()
    all_link= driver.find_elements(By.TAG_NAME, value='a')
    print(f"total link:{len(all_link)}")

    for i in all_link:
        href = i.get_attribute('href')
        response = requests.get(href)
        if response.status_code >= 400:
            print(f"broken line {href} source code:{response.status_code}")

        else:
            print("no link broken")
    driver.close()