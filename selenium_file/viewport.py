import time

from selenium import webdriver
from selenium.webdriver.common.by import By

view_port=[(1024,768),(768,1024),(300,500)]
def test_view():
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")
    try:
        for width, height in view_port:
            driver.set_window_size(width, height)
            time.sleep(2)
    finally:
        driver.close()
