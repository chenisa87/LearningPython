from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC
import time


PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://pornpen.ai/make")

time.sleep(5)

text = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"text-base")),"沒找到元素")
for i in text:
    print(i.text)

driver.quit()