import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service class we can handle the chrome version changes
service_obj =Service("C:\\Users\\Susis\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
time.sleep(3)
#chrome driver service version ,can change based on seleium version
# driver = webdriver.Chrome()
# time.sleep(5)

#path of the chrme verion stable version chrom driver download
