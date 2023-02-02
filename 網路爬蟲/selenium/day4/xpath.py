from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://tw.stock.yahoo.com/")
test = driver.find_element(By.XPATH,"//span[normalize-space()='2303.TW']")
print(test.text)

time.sleep(10)