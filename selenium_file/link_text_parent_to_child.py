from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/auth/password-new")
import time
time.sleep(3)
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("1223")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").click()
