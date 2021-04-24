import time
from selenium import webdriver
from seleniumSwagLabs.pages.LoginPage import LoginPage
from seleniumSwagLabs.pages.HomePage import HomePage
import unittest
from seleniumSwagLabs.strings import strings

class TestLoginCases(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=strings.driver_path)
        cls.driver.maximize_window()
        cls.driver.get(strings.url)

    def test_1_login_wrong_credentials(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(strings.standard_username)
        lp.enter_password("wrong_password")
        lp.click_submit_btn()
        lp.close_credentials_error()

    def test_2_login_right_credentials(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(strings.standard_username)
        lp.enter_password(strings.password)
        lp.click_submit_btn()

    def test_3_logout(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.logout_from_page()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()