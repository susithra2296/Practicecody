from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


def test_view11():
    driver = webdriver.Firefox()
    driver.get("https://demo.automationtesting.in/Datepicker.html")
    time.sleep(5)
    driver.find_element(By.ID, value= "datepicker2").click()
    time.sleep(2)
    current_date = datetime.now()
    print(current_date)

    next_day = current_date + timedelta(days=1)
    print(next_day)

    next_day1 = (str(next_day.day))
    print(next_day1)

    current_month = datetime.now().month
    current_year = current_date.year

    next_month = (current_month % 12) +1
    next_month_year =f"{next_month/current_year}"

    month_dd = driver.find_element(By.CSS_SELECTOR,value="select[title='Change the month']")
    select = Select(month_dd)
    select.select_by_value(str(next_month_year))
    year_dd = driver.find_element(By.CSS_SELECTOR,value="select[title='Change the year']")
    select = Select(year_dd)
    select.select_by_visible_text("2024")
    driver.find_element(By.LINK_TEXT,next_day1).click()
    time.sleep(3)


