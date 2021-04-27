import pytest
from seleniumSwagLabs.pages.LoginPage import LoginPage
from seleniumSwagLabs.pages.HomePage import HomePage
from seleniumSwagLabs.strings import strings

@pytest.mark.usefixtures("init_driver")
class TestBuyItem():

    driver = None

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