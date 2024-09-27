from selenium import webdriver
from selenium.webdriver.common.by import By

def test_first():
    pass

def test_selenium():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get('https://www.facebook.com/')
    email_input = driver.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys("test@text.com")

    pass_input = driver.find_element(By.ID, "pass")
    pass_input.send_keys("test123414")

    driver.find_element(By.NAME, "login").click()
    driver.quit()




