from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://www.google.com.tw/")
driver.maximize_window()
search = driver.find_element(By.NAME,"q").send_keys("python")
time.sleep(5)


