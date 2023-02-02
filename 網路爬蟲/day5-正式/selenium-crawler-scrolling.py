from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.chrome_executable_path = "C:/Users/User/Desktop/chromedriver.exe"
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver=webdriver.Chrome(options=options)

driver.get("https://www.ptt.cc/bbs/hotboards.html")
titles = driver.find_elements(By.CLASS_NAME,"board-title")
for title in titles:
    print(title.text)
driver.close()