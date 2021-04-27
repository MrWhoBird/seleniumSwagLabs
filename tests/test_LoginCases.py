import pytest
from seleniumSwagLabs.pages.LoginPage import LoginPage
from seleniumSwagLabs.pages.HomePage import HomePage
from seleniumSwagLabs.strings import strings
import time

@pytest.mark.usefixtures("init_driver")
class TestLoginCases():

    driver = None

    def test_1_login_wrong_credentials(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(strings.standard_username)
        lp.enter_password("wrong_password")
        lp.click_submit_btn()
        time.sleep(1)
        lp.close_credentials_error()

    def test_2_login_right_credentials(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username(strings.standard_username)
        lp.enter_password(strings.password)
        time.sleep(1)
        lp.click_submit_btn()

    def test_3_logout(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.logout_from_page()