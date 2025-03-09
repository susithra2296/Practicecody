import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_view11():
    browser = webdriver.Firefox()

    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    browser.get(URL)

    browser.maximize_window()

    # button = browser.find_element(By.XPATH, value="//button[normalize-space()='Click for JS Alert']")
    # button.click()
    # alert_page = browser.switch_to.alert
    # time.sleep(2)
    # text = alert_page.text
    # print(text)
    # time.sleep(2)
    # alert_page.accept()
    # alert_page.dismiss()
    button = browser.find_element(By.XPATH, value="//button[normalize-space()='Click for JS Prompt']")
    button.click()
    my_alt = browser.switch_to.alert
    my_alt.send_keys("new alert")
    print(my_alt.text)
    my_alt.accept()

