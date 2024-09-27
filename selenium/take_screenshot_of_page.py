from selenium import webdriver
from selenium.webdriver.common.by import By



def test_take_screenshot_of_page():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com/')

    driver.save_screenshot("screen.png")
    image_code = driver.get_screenshot_as_base64()
    print(image_code)

    driver.find_element(By.XPATH,'//img[@alt= "Facebook"]').screenshot("logo.png")








