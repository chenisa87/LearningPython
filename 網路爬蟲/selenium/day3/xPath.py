from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://www.python.org/")


driver.find_element(By.XPATH,'//input[@id="id-search-field" or @placeholder="Search"]').send_keys("abc")
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
time.sleep(10)

