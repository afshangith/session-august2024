from selenium import webdriver
from selenium.webdriver.common.by import By


def test_download():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://the-internet.herokuapp.com/download')
    driver.implicitly_wait(10)

    driver.find_element(By.LINK_TEXT,"LambdaTest.txt").click()


def test_upload():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://the-internet.herokuapp.com/upload')
    driver.implicitly_wait(10)


    element = driver.find_element(By.ID, "file-upload")
    element.send_keys("C:\\Users\\12149\\Downloads\\LambdaTest.txt")

    driver.find_element(By.ID,"file-submit").click()
    message = driver.find_element(By.TAG_NAME, "h3").text
    assert message == "File Uploaded!"

    driver.quit()







