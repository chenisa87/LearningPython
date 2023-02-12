from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init(self,driver:WebDriver):
        self.driver = driver

    def apply_star_raing(self):
        self.driver.find_element(By.ID,"")