import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains




@pytest.fixture
def first_value():
    print("Before Method")
    yield
    print("After method")


def test_assert1(first_value):
    action = ActionChains(driver)
    source_element = driver.find_element(By.ID, "draggable")
    target_element = driver.find_element(By.ID, "droppable")
    action.drag_and_drop(source_element, target_element).perform()

def test_assert2(first_value):
    print("TestB")









