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

def execute_qs(driver, selector):
    script = "document.querySelector('" + selector + "').click()"
    driver.execute_script(script)

def test_DE_login():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)

    driver.get("https://storefront:horze123@hrzde.sta.horze.io/on/demandware.store/Sites-hrzde-Site/de_DE/Login-Form")

    driver.maximize_window()

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('button:last-child').click()"
    driver.execute_script(acceptUC)
    
    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    
    email = driver.find_element_by_name("username")
    email.send_keys("login@gmail.com")
    time.sleep(3)
    password = driver.find_element_by_name("password")
    password.send_keys("login@gmail.com")
    time.sleep(2)

    driver.find_element_by_name("dwfrm_login_login").click()
    
    time.sleep(5)

    result = driver.find_element_by_link_text("Meine Anfragen")

    assert result.is_displayed() == True

    time.sleep(2)

    driver.close()