import time
import pytest
from selenium import webdriver
from seleniumSwagLabs.pages.LoginPage import LoginPage
from seleniumSwagLabs.pages.HomePage import HomePage
import unittest
from seleniumSwagLabs.strings import strings

class TestLoginCases():

    #driver = None

    @pytest.fixture(autouse=True)
    def test_setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=strings.driver_path)
        self.driver.maximize_window()
        self.driver.get(strings.url)
        yield
        time.sleep(3)
        self.driver.quit()

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
        lp = LoginPage(driver)
        lp.enter_username(strings.standard_username)
        lp.enter_password(strings.password)
        lp.click_submit_btn()
        hp = HomePage(driver)
        hp.logout_from_page()

if __name__ == '__main__':
    unittest.main()