from selenium.webdriver.common.by import By
from seleniumSwagLabs.strings import strings

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(by=By.ID, value=strings.username_textbox_id).clear()
        self.driver.find_element(by=By.ID, value=strings.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(by=By.ID, value=strings.password_textbox_id).clear()
        self.driver.find_element(by=By.ID, value=strings.password_textbox_id).send_keys(password)

    def click_submit_btn(self):
        self.driver.find_element(by=By.ID, value=strings.login_button_id).click()

    def close_credentials_error(self):
        self.driver.find_element(by=By.CLASS_NAME, value=strings.close_wrong_credentials_error_class).click()