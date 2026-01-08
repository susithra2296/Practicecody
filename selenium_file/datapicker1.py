from datetime import datetime, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

def test_view11():
    browser = webdriver.Chrome()

    URL = "https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker"

    browser.get(URL)
    time.sleep(4)
    browser.find_element(By.XPATH, value="//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()

    frame_lo = browser.find_element(By.XPATH,value="//iframe[@class='demo-frame lazyloaded']")
    browser.switch_to.frame(frame_lo)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, value="#datepicker").click()

    current_date = datetime.now()

    next_data = current_date + timedelta(days=1)

    formate_date = next_data.strftime("%m/%d/%y")

    test = browser.find_element(By.CSS_SELECTOR, value="#datepicker")
    test.send_keys(formate_date + Keys.TAB)




