from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

searchbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']")),"找不到指定元素")

print("Display status",searchbox.is_displayed())
print("Enabled status",searchbox.is_enabled())
print("Display status",searchbox.is_displayed())

driver.quit()