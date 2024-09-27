
from selenium import webdriver
from selenium.webdriver.common.by import By

#browser = webdriver.Firefox()
#browser = webdriver.Edge()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.facebook.com/')
email_input = driver.find_element(By.ID, "email")
email_input.clear()
email_input.send_keys("test@text.com")

pass_input = driver.find_element(By.ID, "pass")
pass_input.send_keys("test123414")

driver.find_element(By.NAME, "login").click()



#driver.quit() in python the exection/run usually closes the window
# even though we don't hit the quit a spl code has to be writtten to stop the closing