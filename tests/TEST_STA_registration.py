from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
import time
# import pytest
import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
import random

def execute_qs(driver, selector):
    script = "document.querySelector('" + selector + "').click()"
    driver.execute_script(script)

def test_DE_registration():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)

    driver.get("https://storefront:horze123@hrzde.sta.horze.io/registrieren")

    driver.maximize_window()

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('button:last-child').click()"
    driver.execute_script(acceptUC)
    
    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    
    firstName = driver.find_element_by_id("firstName")
    firstName.send_keys("test")
    time.sleep(2)
    lastName = driver.find_element_by_id("lastName")
    lastName.send_keys("test")
    time.sleep(2)
    n = random.randint(333, 999)
    email = driver.find_element_by_id("email")
    email.send_keys(n)
    email.send_keys("@gmail.com")
    time.sleep(2)
    password = driver.find_element_by_id("password")
    password.send_keys("Test123Test123!@#$")
    time.sleep(2)
    driver.find_element_by_id("marketing").click()
    time.sleep(2)
    execute_qs(driver, "#RegistrationForm button")
    
    time.sleep(5)

    result = driver.find_element_by_link_text("Meine Anfragen")

    assert result.is_displayed() == True

    time.sleep(2)

    driver.close()