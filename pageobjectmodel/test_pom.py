from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageobjectmodel.test_login_page import *

def test_log():

    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    time.sleep(3)
    test_login1 = test_login(driver)
    test_login1.login()