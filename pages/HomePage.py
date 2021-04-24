import time
from selenium.webdriver.common.by import By
from seleniumSwagLabs.strings import strings
import random

class HomePage():

    def __init__(self,driver):
        self.driver = driver

    def logout_from_page(self):
        self.driver.find_element(by=By.ID, value=strings.burger_button_id).click()
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=strings.logout_button_id).click()

    def buy_item(self):
        btn_div_val = "/html/body/div/div/div/div[2]/div/div/div/div["+str(random.randrange(1,6,1))+"]/div[2]/div[2]/button"
        button = self.driver.find_element(by=By.XPATH, value=btn_div_val)
        button.click()
        time.sleep(3)
