from selenium import webdriver
from selenium.webdriver.common.by import By


def test_tab_handle():
    driver = webdriver.Firefox()
    driver.get("https://www.selenium.dev/downloads/")
    driver.maximize_window()
    driver.switch_to.new_window()
    driver.get("https://playwright.dev/docs/intro")
    total_tab = len(driver.window_handles)
    print(total_tab)
    tab_value = driver.window_handles
    print(tab_value)
    current_tab = driver.current_window_handle
    print(current_tab)
    first_tab = driver.window_handles[0]

    if current_tab != first_tab:
        driver.switch_to.window(first_tab)
    driver.find_element(By.CSS_SELECTOR, value= "//span[normalize-space()='Downloads']")



