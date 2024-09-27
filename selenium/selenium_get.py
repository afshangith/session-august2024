
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_get_value():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com/')
    title = driver.title
    assert title == "Facebook - log in or sign up"

    driver.find_element(By.LINK_TEXT,"Forgot password?").click()
    url = driver.current_url
    assert url.find("facebook_login")

    print(driver.page_source)


def test_get_element_value():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com/')

    text_desc = driver.find_element(By.TAG_NAME, "h2").text
    assert text_desc == "Connect with friends and the world around you on Facebook."

    email_place_holder = driver.find_element(By.ID,"email").get_attribute("placeholder")
    assert email_place_holder == "Email or phone number"
    password_place_holder = driver.find_element(By.ID, "pass").get_attribute("placeholder")
    assert password_place_holder == "Password"

    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").get_attribute("href")
    print(link)

    login_element = driver.find_element(By.NAME, "login")
    border_radius = login_element.value_of_css_property("border-radius")
    print(border_radius)
    font_size = login_element.value_of_css_property("font-size")
    print(font_size)
    line_height = login_element.value_of_css_property("line-height")
    print(line_height)
    padding = login_element.value_of_css_property("padding")
    print(padding)
    width = login_element.value_of_css_property("width")
    print(width)









