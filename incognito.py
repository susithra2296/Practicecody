import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_view11():

    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    # firefox_option.add_argument("--Private")

    driver = webdriver.Chrome(options=chrome_option)
    time.sleep(5)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(5)