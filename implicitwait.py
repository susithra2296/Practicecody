from selenium import webdriver
from selenium.webdriver.common.by import By

def test_lamda_test2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get("https://www.selenium.dev/")
    print("Title:", driver.title)
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