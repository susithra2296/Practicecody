from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sample1():
    browser = webdriver.Firefox()
    browser.get("https://cosmocode.io/automation-practice-webtable/")
    browser.maximize_window()
    browser.execute_script("window.scrollTo(0,700)")
    row = browser.find_elements(By.TAG_NAME, value="tr")
    row_count =len(row)
    print(row_count)
    target_value = "Australia"
    found = False
    for i in row:
        cell = i.find_elements(By.TAG_NAME, value="td")
        for j in cell:
            if target_value in j.text:
                print(f"found : {target_value}")
                print(j.text)
                found = True
                break
        if found:
            break
    if not found:
        print(f"not found{target_value}")