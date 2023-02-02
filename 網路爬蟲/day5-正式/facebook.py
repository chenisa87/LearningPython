from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.chrome_executable_path = "C:/Users/User/Desktop/chromedriver.exe"
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/messages/t/5209927225689737") #到那個網站

email = driver.find_element("id","email")
password = driver.find_element("id","pass")

email.send_keys("aa920308@yahoo.com.tw")
password.send_keys("aa02765258")
password.submit()



time.sleep(10)
driver.quit()
