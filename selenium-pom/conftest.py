import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver


@pytest.fixture(scope="class")
def set_up(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    #driver = EventFiringWebDriver(driver, MyListner())
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def navigate_url(request):
        request.cls.driver.get("https://www.jcpenney.com/")


