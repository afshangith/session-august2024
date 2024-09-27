from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_button_actions():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/buttons')

    action = ActionChains(driver)
    double_click_button = driver.find_element(By.ID,"doubleClickBtn")
    action.double_click(double_click_button).perform()
    assert "You have done a double click" ==  driver.find_element(By.ID,"doubleClickMessage").text

    action.context_click(driver.find_element(By.ID,"rightClickBtn")).perform()
    assert "You have done a right click" ==  driver.find_element(By.ID,"rightClickMessage").text

    action.click(driver.find_element(By.XPATH, "//button[text()='Click Me']")).perform()
    assert "You have done a dynamic click" == driver.find_element(By.ID, "dynamicClickMessage").text

    driver.quit()

    




