import time
from selenium import webdriver
from RaghavYT_UnitTest.pages.LoginPage import LoginPage
from RaghavYT_UnitTest.pages.HomePage import HomePage
import unittest
from RaghavYT_UnitTest.strings import strings

class TestLoginAndLogout(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=strings.driver_path)
        cls.driver.maximize_window()
        cls.driver.get(strings.url)

    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(strings.standard_username)
        lp.enter_password(strings.password)
        lp.click_submit_btn()

    def test_logout(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.logout_from_page()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()