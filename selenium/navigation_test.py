from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_navigation():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://demoqa.com/browser-windows')

    driver.get('https://facebook.com')
    driver.find_element(By.LINK_TEXT,"Forgot password?").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()





