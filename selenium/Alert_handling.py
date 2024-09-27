from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_handle_alert():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')

    driver.find_element(By.XPATH , "//button[text()='Click for JS Alert']").click()
    alert = Alert(driver)
    print(alert.text)
    assert alert.text == "I am a JS Alert"
    alert.accept()
    driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
    alert = Alert(driver)
    print(alert.text)
    alert.dismiss()
    assert driver.find_element(By.ID,"result").text =="You clicked: Cancel"
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = Alert(driver)
    print(alert.text)
    alert.send_keys("Alert Text")
    alert.accept()
    assert driver.find_element(By.ID, "result").text == "You entered: Alert Text"


def test_explicit():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/alerts')
    alert_button = driver.find_element(By.ID,"timerAlertButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_button)
    alert_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    print(alert.text)

    #WebDriverWait(driver, 30).until(EC.presence_of_element_located(By.ID,""))
    #WebDriverWait(driver, 30).until(EC.







