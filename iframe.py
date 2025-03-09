from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


def test_view11():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.maximize_window()
    frame=driver.find_element(By.ID,value="mce_0_ifr")
    driver.switch_to.frame(frame)

    frame_content = driver.find_element(By.ID, value="tinymce")
    frame_content.clear()
    frame_content.send_keys("new page")
    time.sleep(2)
    driver.switch_to.default_content()
