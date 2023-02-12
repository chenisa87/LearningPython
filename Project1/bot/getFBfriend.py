from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from booking import constants as const

PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=PATH ,options=option)
driver.implicitly_wait(15)

driver.get("https://www.facebook.com/")
email = driver.find_element(By.NAME,"email")
passw = driver.find_element(By.NAME,"pass")
email.send_keys(const.EMAIL)
passw.send_keys(const.PASS)
email.click()
passw.click()
btn = driver.find_element(By.NAME,"login")
btn.click()
driver.get("https://www.facebook.com/friends/list")
action = ActionChains(driver)
action.move_by_offset(100,200).click().perform()
friends = driver.find_elements(By.CLASS_NAME,"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen x1s688f xzsf02u")
for friend in friends:
    print(friend.text)

print("結束")
driver.quit()
