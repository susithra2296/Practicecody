
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium_test3():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.maximize_window()
    username="standard_user"
    password="secret_sauce"
    username_field= driver.find_element(By.ID,value="user-name")
    password_filed= driver.find_element(By.ID,value="password")
    username_field.send_keys(username)
    password_filed.send_keys(password)
    login_filed = driver.find_element(By.ID,value="login-button")
    assert not login_filed.get_attribute("disable")
    login_filed.click()
    page_tittle= driver.find_element(By.CSS_SELECTOR,value=".product_label")
    assert page_tittle.text == "Products"




