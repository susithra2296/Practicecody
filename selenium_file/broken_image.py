import requests
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


def test_view2():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/broken_images")
    time.sleep(2)
    driver.maximize_window()
    images=driver.find_elements(By.TAG_NAME,value="img")
    broken_images=[]

    for image in images:
        src = image.get_attribute("src")
        if src:
            response = requests.get(src)
            if response.status_code != 200:
                broken_images.append(src)
                print(f"broken image found")
    if broken_images:
        print("list of broken image")
        for broken_image in broken_images:
            print(broken_image)

    else:
        print("no broken image")