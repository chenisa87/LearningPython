from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://www.google.com.tw/")

print(driver.title)
print(driver.current_url)

search = driver.find_element(By.NAME,"q")
search.send_keys("python")

ActionChains(driver).move_to_element(search).key_down(Keys.ENTER).perform()
driver.quit()