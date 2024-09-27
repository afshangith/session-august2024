from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pytest

@pytest.fixture
def set_up():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    global driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/droppable')
    yield
    driver.quit()


def test_assert1(set_up):
    action = ActionChains(driver)
    source_element = driver.find_element(By.ID, "draggable")
    target_element = driver.find_element(By.ID, "droppable")
    action.drag_and_drop(source_element, target_element).perform()

def test_assert2(set_up):
    print("TestB")