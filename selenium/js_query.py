
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


def test_js():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://demoqa.com/alerts')

    #tab opening
    alert_button = driver.find_element(By.ID,"alertButton")
    #driver.execute_script("arguments[0].click();" , alert_button)
    #driver.execute_script('document.getElementById("alertButton").click()')
    #driver.execute_script("arguments[0].scrollIntoView(true);", alert_button)
    driver.execute_script("window.scrollTo(0, 1000);")
    alert_button.click();

