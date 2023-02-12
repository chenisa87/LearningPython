from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import booking.constants as const
import time
from booking.booking_filtitration import BookingFiltration
PATH = const.CHROME_URL
service = Service(PATH)

#讓網頁不再自己跳掉
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)


class Booking(webdriver.Chrome):
    def __init__(self,service=service ,option = option , teardown=False):
        os.environ["PATH"] += PATH
        self.teardown = teardown
        super(Booking,self).__init__(service=service , options=option)
        # 每次等待15秒 直到時間結束或者找到該元素
        self.implicitly_wait(15)
        self.maximize_window()


    # >>> 通常與 with statement 配合使用 在結束的時自動使用 <<< #
    def __exit__(self , exc_type , exc_val , exc_tb):
        # 這是一個開關來控制要不要關閉網頁 
        if self.teardown:
            self.quit()

    def clickw(self):
        action = ActionChains(self)
        action.move_by_offset(100,200).click().perform()


    def login(self):
        self.get(const.BASE_URL)
        email = self.find_element(By.NAME,"email")
        passw = self.find_element(By.NAME,"pass")

        email.send_keys(const.EMAIL)
        passw.send_keys(const.PASS)

        email.click()
        passw.click()

        btn = self.find_element(By.NAME,"login")
        btn.click()

        action = ActionChains(self)
        action.move_by_offset(100,200).click().perform()

        mess = self.find_element(By.XPATH,"//a[@href='https://www.facebook.com/messages/t/']//div[@class='x6s0dn4 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1q0g3np x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r xeuugli x18d9i69 x1sxyh0 xurb0ha xexx8yu x1n2onr6 x1ja2u2z x1gg8mnh']//div[@class='x6s0dn4 xkh2ocl x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1q0g3np x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x18d9i69 x4uap5 xkhd6sd xexx8yu x1n2onr6 x1ja2u2z']//div[@class='x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1r8uery x1iyjqo2 xs83m0k x1qughib x11i5rnm x1mh8g0r x2lwn1j xeuugli x4uap5 xkhd6sd x1n2onr6 x1ja2u2z x1qjc9v5 xdt5ytf xat24cr xdj266r xz9dl7a xsag5q8']")
        mess.click()


    def findpeople(self,people):
        search = self.find_element(By.XPATH,"//input[@placeholder='搜尋 Messenger']")
        search.send_keys(people)
        time.sleep(5)
        ActionChains(self).move_by_offset(78,20).click().perform()


        #尋找座標
        """
        search = self.find_element(By.XPATH,f"//li[@id='100023847227339']//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'][contains(text(),'{people}')]")
        location = search.location
        x = location["x"]
        y = location["y"]
        print(x,y)
        search.click()
        """

    def sendmessage(self,message):
        inputm = self.find_element(By.XPATH,"//p[@class='xat24cr xdj266r']")
        inputm.send_keys(message)
        inputm.send_keys(Keys.ENTER)
        

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)






        


