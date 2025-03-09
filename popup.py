from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium_test():
    driver = webdriver.Firefox()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, value="//button[@id='alertBtn']").click()
    my_alt = driver.switch_to.alert
    print(my_alt.text)
    my_alt.accept()