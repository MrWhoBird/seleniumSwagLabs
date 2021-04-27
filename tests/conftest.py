from selenium import webdriver
from seleniumSwagLabs.strings import strings
import time
import pytest

@pytest.fixture(scope='class')
def init_driver(request):
    driver = webdriver.Chrome(executable_path=strings.driver_path)
    request.cls.driver = driver
    driver.maximize_window()
    driver.get(strings.url)
    yield
    time.sleep(1)
    driver.quit()