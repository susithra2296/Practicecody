import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_browser_test2():
    driver=webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    driver.close()

