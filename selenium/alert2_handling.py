import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

def test_handle_alert():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)


    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(16)
    driver.get('https://demoqa.com/alerts')

    driver.find_element(By.ID,"alertButton").click()
    alert = Alert(driver)
    print(alert.text)
    assert alert.text == 'You clicked a button'
    alert.accept()

    driver.find_element(By.ID, "timerAlertButton").click()
    alert = Alert(driver)
    time.sleep(6)
    print(alert.text)
    assert alert.text == 'This alert appeared after 5 seconds'
    alert.accept()

    driver.find_element(By.ID, "confirmButton").click()
    alert = Alert(driver)
    print(alert.text)
    alert.dismiss()
    assert driver.find_element(By.ID,"confirmResult").text == "You selected Cancel"

    driver.find_element(By.ID, "promtButton").click()
    alert = Alert(driver)
    print(alert.text)
    alert.send_keys("Afshan")
    alert.accept()
    assert driver.find_element(By.ID, "promptResult").text == "You entered Afshan"














