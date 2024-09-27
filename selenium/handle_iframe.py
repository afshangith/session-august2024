from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

def test_handle_iframe():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/frames')
    main_content = driver.find_element(By.XPATH, '//div[@id="framesWrapper"]/div[1]').text
    print(main_content)

    driver.switch_to.frame("frame1")
    frame_text = driver.find_element(By.ID, "sampleHeading").text
    print(frame_text)

    driver.switch_to.parent_frame()
    main_content = driver.find_element(By.XPATH, '//div[@id="framesWrapper"]/div[1]').text
    print(main_content)


def test_handle_nestediframe():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/nestedframes')
    main_content = driver.find_element(By.XPATH,'//div[@id="framesWrapper"]/div[1]').text
    print(main_content)


    driver.switch_to.frame("frame1")
    frame_text = driver.find_element(By.TAG_NAME, "body").text
    print(frame_text)

    driver.switch_to.frame(0)#via indexing starting 0
    child_frame_text = driver.find_element(By.TAG_NAME,"p").text
    print(child_frame_text)

    #driver.switch_to.prent_frame()
    driver.switch_to.default_content()
    main_content = driver.find_element(By.XPATH, '//div[@id="framesWrapper"]/div[1]').text
    print(main_content)




