from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://www.google.com.tw/")
driver.maximize_window()

actions = ActionChains(driver)

searchbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"gLFyf")),"找不到指定元素")
actions.move_to_element(driver.find_element(By.CLASS_NAME,"gLFyf")).click().send_keys("比特幣").perform()
searchbox.submit()
time.sleep(10)

driver.quit()