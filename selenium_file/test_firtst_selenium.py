from selenium import webdriver
from selenium.webdriver.common.by import By

# def test_lamda_test():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.flightradar24.com/data/airports/pnq")
#     print("Title:", driver.title)
#     # get element
#     # element = driver.find_element(By.LINK_TEXT, "Text of Link")
#     element = driver.find_element('//*[@class ="hide-mobile-only ng-binding"]')
#     # get text
#     print(element.text)
#
#     driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# browser = webdriver.Firefox()
#
# browser.get('http://www.yahoo.com')
# assert 'Yahoo' in browser.title
#
# elem = browser.find_element(By.NAME, 'p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
#
# browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("https://www.python.org")
# print(driver.title)
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()
def test_lamda_test2():
    driver = webdriver.Chrome()
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
