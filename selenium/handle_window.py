from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

def test_handle_window():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://demoqa.com/browser-windows')

    #tab opening
    driver.find_element(By.ID,"tabButton").click()
    win_id = driver.current_window_handle

    for handle in driver.window_handles:
        driver._switch_to.window(handle)

    text_child_tab = driver.find_element(By.ID, "sampleHeading").text
    print(text_child_tab)
    driver.close()

    driver._switch_to.window(win_id)
    parent_win_text = driver.find_element(By.XPATH,'//h1[@class="text-center"]').text
    print(parent_win_text)

    driver.quit()

def test_open_tab_window():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://demoqa.com/browser-windows')

    driver.switch_to.new_window('tab')
    driver.get('https://facebook.com')

    driver.switch_to.new_window('window')
    driver.get('https://google.com')


