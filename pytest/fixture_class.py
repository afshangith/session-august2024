import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def set_up(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("set_up")
class BaseTest:
    pass

class Test_Selenium_Example(BaseTest):


    def test_selenium1(self):
        pass

    def test_selenium2(self):
        pass

