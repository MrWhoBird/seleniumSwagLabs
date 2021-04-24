import time
from selenium.webdriver.common.by import By
from RaghavYT_UnitTest.strings import strings

class HomePage():

    def __init__(self,driver):
        self.driver = driver

    def logout_from_page(self):
        self.driver.find_element(by=By.ID, value=strings.burger_button_id).click()
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=strings.logout_button_id).click()