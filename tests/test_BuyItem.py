import time
from selenium import webdriver
from seleniumSwagLabs.pages.LoginPage import LoginPage
from seleniumSwagLabs.pages.HomePage import HomePage
import unittest
from seleniumSwagLabs.strings import strings

class TestBuyItem(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=strings.driver_path)
        cls.driver.maximize_window()
        cls.driver.get(strings.url)

    def test_buy_item(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(strings.standard_username)
        lp.enter_password(strings.password)
        lp.click_submit_btn()
        print("login OK")
        hp = HomePage(driver)
        hp.buy_item()
        print("buy_item OK")

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()