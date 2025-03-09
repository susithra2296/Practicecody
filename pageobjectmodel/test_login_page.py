from selenium import webdriver
from selenium.webdriver.common.by import By


class test_login:
    def __init__(self,driver):
        self.driver = driver
        self.user = (By.NAME, "email")
        self.passw = (By.ID, "exampleInputPassword1")
        self.sign = (By.ID, "exampleCheck1")


    def login(self):
        self.driver.find_element(*self.user).send_keys("susi.sooriya@gmail.com")
        self.driver.find_element(*self.passw).send_keys("test123")
        self.driver.find_element(*self.sign).click()



