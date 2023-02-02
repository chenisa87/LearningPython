from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:/Users/User/Desktop/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.dcard.tw/f")

titles = driver.find_elements(By.CLASS_NAME,"atm_cs_1urozh atm_c8_1csq7v7 atm_g3_1qqjw7d atm_7l_1pday2 atm_1938jqx_1yyfdc7 atm_2zt8x3_stnw88 atm_grwvqw_gknzbh atm_1ymp90q_idpfg4 atm_89ifzh_idpfg4 atm_1hh4tvs_1osqo2v atm_1054lsl_1osqo2v t1gihpsa")


for title in titles:
    print(title.text)

time.sleep(10)
driver.close()