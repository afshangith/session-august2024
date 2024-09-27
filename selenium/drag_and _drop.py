from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_drag_drop():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/droppable')

    action = ActionChains(driver)
    source_element = driver.find_element(By.ID,"draggable")
    target_element = driver.find_element(By.ID, "droppable")
    action.drag_and_drop(source_element, target_element).perform()


def test_drag_drop_by():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/dragabble')

    action = ActionChains(driver)
    source_element = driver.find_element(By.ID,"dragBox")
    action.drag_and_drop_by_offset(source_element, 300,15).perform()




