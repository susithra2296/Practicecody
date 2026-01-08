import time

from selenium import webdriver

from selenium.webdriver.common.by import By
import csv


def test_view11():
    csv_file = "test_data1.csv"
    test_data=[]
    with open(csv_file,'r') as file:
        reader =csv.DictReader(file)
        for row in reader:
            test_data.append(row)

    for data in test_data:

        driver = webdriver.Firefox()
        driver.get("https://www.saucedemo.com/v1/index.html")
        driver.maximize_window()
        time.sleep(2)
        username_field = driver.find_element(By.ID, value="user-name").send_keys(data['username'])
        password_filed = driver.find_element(By.ID, value="password").send_keys(data['password'])
        login_filed = driver.find_element(By.ID, value="login-button")
        assert not login_filed.get_attribute("disable")
        login_filed.click()
