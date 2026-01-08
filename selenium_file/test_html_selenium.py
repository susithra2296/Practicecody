import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium_test3():
    driver = webdriver.Firefox()

    # Load the HTML file (adjust the path as needed)
    driver.get("C:\\Users\\Susis\\PycharmProjects\\pythonProject\\Demoselenium\\test_html.html")
    time.sleep(5)
    # Fetch the main title
    main_title = driver.find_element(By.ID, "main-title").text
    print(f"Main Title: {main_title}")

    # Fetch the alt text of the first image in the gallery
    first_image_alt = driver.find_element(By.CSS_SELECTOR, ".gallery img").get_attribute("alt")
    print(f"First Image Alt Text: {first_image_alt}")

    # Fetch all links and their titles
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        link_text = link.text
        link_title = link.get_attribute("title")
        print(f"Link: {link_text}, Title: {link_title}")

    # Fetch the copyright text
    copyright_text = driver.find_element(By.CSS_SELECTOR, "footer p").text
    print(f"Copyright Text: {copyright_text}")

    # Close the browser
    driver.quit()

