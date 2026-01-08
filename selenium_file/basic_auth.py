from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

def test_view11():
    driver = webdriver.Firefox()
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.maximize_window()
    usename = "admin"
    password = "admin"

#https:/admin:admin@domain/path

    