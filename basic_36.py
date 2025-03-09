from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME, value="email").send_keys("susi.sooriya@gmail.com")
driver.find_element(By.ID, value="exampleInputPassword1").send_keys("test123")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("test123") #id .class
driver.find_element(By.ID, value="exampleCheck1").click()
driver.find_element(By.XPATH, value="//input[@value='Submit']").click()
output = driver.find_element(By.CLASS_NAME, value="alert-success").text
print(output)

assert "Success" in output, "Failed to find msg"
##//tagname[@attribute = "value"]
sel = driver.find_element(By.ID, value="exampleFormControlSelect1")
select = Select(sel)
select.select_by_visible_text("Female")

