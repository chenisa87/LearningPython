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



WebDriverWait(driver,10).until(EC.title_contains("登入"),"還沒跑好")

user = driver.find_element(By.XPATH,"//*[@id='email']")
password = driver.find_element(By.XPATH,"//*[@id='pass']")
user.send_keys("aa920308@yahoo.com.tw")
password.send_keys("aa02765258")
btn = driver.find_element(By.XPATH,"//*[@name='login']")
btn.click()

WebDriverWait(driver,10).until(EC.title_contains("Ins"),"還沒跑好")
#login = driver.find_elements(By.CSS_SELECTOR,"div:contains('chenisa87')")
actions = AC(driver)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR,"div:contains('chenisa87')")).move_to_element_with_offset(30,0).perform()

#print(login)

#
#password.send_keys("aa02765258")
#password.send_keys(Keys.RETURN)

time.sleep(1000)

