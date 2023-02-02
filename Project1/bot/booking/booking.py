from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import booking.constants as const
import time

PATH = const.CHROME_URL
service = Service(PATH)

class Booking(webdriver.Chrome):
    def __init__(self,service=service):
        os.environ["PATH"] += PATH
        super(Booking,self).__init__(service=service)

    def land_first_page(self):
        self.get(const.BASE_URL)
        time.sleep(10)


