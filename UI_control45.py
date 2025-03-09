import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.XPATH,value="//input[@value='option3']").click()
time.sleep(3)
checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxs))

for checkbox in checkboxs:
    checkbox.get_attribute('value') == "option2"
    checkbox.click()
    assert checkbox.is_selected()
    break
