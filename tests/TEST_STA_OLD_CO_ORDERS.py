from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def execute_qs(driver, selector):
    script = "document.querySelector('" + selector + "').click()"
    driver.execute_script(script)

def test_UK_order_paypal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://storefront:horze123@hrzuk.sta.horze.io/womens-full-seat-breeches/horze-active-womens-silicone-grip-full-seat-breeches/36277.html")

    driver.maximize_window()

    time.sleep(5)

    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # select size
    execute_qs(driver, "#size-select > div")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(1)")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    time.sleep(4)          
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(5)
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div.bg-white.p-15.p-sm-30.mb-sm-30 > div > div > div > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div:nth-child(3) > a")
    time.sleep(3)
    driver.execute_script("document.querySelector('body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > div.form-group > div.c-custom-field > input').value='test@gmail.com'")
    driver.execute_script("document.querySelector('#firstName').value='test'")
    driver.execute_script("document.querySelector('#lastName').value='test'")
    driver.execute_script("document.querySelector('#address1').value='test'")
    driver.execute_script("document.querySelector('#address2').value='test'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pcode = driver.find_element_by_id("postalCode")
    pcode.send_keys("W13 3BG")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='123123123'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
    paypp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[4]/div/label/div[2]/div/div/iframe")
    driver.switch_to.frame(paypp)
    time.sleep(4)


    driver.execute_script("document.querySelector('.paypal-button-label-container').click()")

    wait.until(EC.number_of_windows_to_be(2))


    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(10)        
    email = driver.find_element_by_id("email")
    email.send_keys("johann_1317033282_per@finntack.com")

    execute_qs(driver, "#btnNext")
    time.sleep(4)

    pswrd = driver.find_element_by_id("password")
    pswrd.send_keys("123qweasd")   

    execute_qs(driver, "#btnLogin")
    time.sleep(10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    execute_qs(driver, "#consentButton")

    driver.switch_to.window(original_window)
    
    # time.sleep(10)
    # execute_qs(driver, "body > div.container.my-60 > div > div.col-12.col-md-8 > div.row.justify-content-center.justify-content-sm-between.mt-30.mb-15 > div > a")
    time.sleep(8)

    result = driver.find_element_by_link_text("Your Orders")
    
    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()




def test_UK_order_klarna_paylater():
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    # wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzuk.sta.horze.io/womens-full-seat-breeches/horze-active-womens-silicone-grip-full-seat-breeches/36277.html")

    driver.maximize_window()

    time.sleep(5)
    
    # original_window = driver.current_window_handle
    # assert len(driver.window_handles) == 1
    # time.sleep(4)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
     # select size
    execute_qs(driver, "#size-select > div")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(1)")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    time.sleep(4)          
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(5)
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div.bg-white.p-15.p-sm-30.mb-sm-30 > div > div > div > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div:nth-child(3) > a")
    time.sleep(3)
    driver.execute_script("document.querySelector('body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > div.form-group > div.c-custom-field > input').value='test@gmail.com'")
    driver.execute_script("document.querySelector('#firstName').value='test'")
    driver.execute_script("document.querySelector('#lastName').value='test'")
    driver.execute_script("document.querySelector('#address1').value='test'")
    driver.execute_script("document.querySelector('#address2').value='test'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pcode = driver.find_element_by_id("postalCode")
    pcode.send_keys("W13 3BG")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='123123123'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)   
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.offset-lg-1.mb-15 > div:nth-child(3) > label")
    time.sleep(3)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div.row.payment-method-fragment-js > div.col-12.col-sm-6.col-lg-4.c-totals.c-totals--float.floating-totals-js.offset-sm-6.mb-15.px-0 > div > label > a")


    time.sleep(10)
    result = driver.find_element_by_link_text("Horze Durable Saddle Rack")

    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()    



def test_UK_order_CC():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzuk.sta.horze.io/stands-racks/horze-durable-saddle-rack/50000.html")

    driver.maximize_window()

    time.sleep(5)
    
    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1
    time.sleep(4)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # change color
    
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div > div > div > div > div:nth-child(2) > div > div > div > label")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    time.sleep(4)          
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(5)
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div.bg-white.p-15.p-sm-30.mb-sm-30 > div > div > div > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div:nth-child(3) > a")
    time.sleep(3)
    driver.execute_script("document.querySelector('body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > div.form-group > div.c-custom-field > input').value='test@gmail.com'")
    driver.execute_script("document.querySelector('#firstName').value='test'")
    driver.execute_script("document.querySelector('#lastName').value='test'")
    driver.execute_script("document.querySelector('#address1').value='test'")
    driver.execute_script("document.querySelector('#address2').value='test'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pcode = driver.find_element_by_id("postalCode")
    pcode.send_keys("W13 3BG")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='123123123'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.offset-lg-1.mb-15 > div:nth-child(2) > label")
    time.sleep(3)

    name = driver.find_element_by_id("braintreeCardOwner")
    name.send_keys("test test")

    time.sleep(4)
    ele = driver.find_element_by_xpath("//*[@id='braintree-hosted-field-number']")

    driver.switch_to.frame(ele)
    time.sleep(3)

    cardnumber = driver.find_element_by_id("credit-card-number")
    cardnumber.send_keys("4111 1111 1111 1111")
    time.sleep(3)
    driver.switch_to.default_content()
    time.sleep(4)
    ele1 = driver.find_element_by_xpath("//*[@id='braintree-hosted-field-expirationDate']")
    driver.switch_to.frame(ele1)
    time.sleep(4)
    expiration = driver.find_element_by_id("expiration")
    expiration.send_keys("12/25")
    driver.switch_to.default_content()
    ele2 = driver.find_element_by_xpath("//*[@id='braintree-hosted-field-cvv']")
    driver.switch_to.frame(ele2)
    time.sleep(4)
    cvc = driver.find_element_by_id("cvv")
    cvc.send_keys("123")
    driver.switch_to.default_content()
    time.sleep(4)

    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div.row.payment-method-fragment-js > div.col-12.col-sm-6.col-lg-4.c-totals.c-totals--float.floating-totals-js.offset-sm-6.mb-15.px-0 > div > label > a")
    

    time.sleep(10)
    result = driver.find_element_by_link_text("Your Orders")

    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()    




def test_FR_order_PayPal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzfr.sta.horze.io/pantalon-dequitation-grip---femme/pantalon-dequitation-taille-haute-horze-tara-silicone-fond-integral-femme/36091.html#color=VDB")

    driver.maximize_window()

    time.sleep(5)
    
    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1
    time.sleep(4)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # select size
    execute_qs(driver, "#size-select > div")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(1)")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    time.sleep(3)
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(5)
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div.bg-white.p-15.p-sm-30.mb-sm-30 > div > div > div > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div:nth-child(3) > a")
    time.sleep(3)
    driver.execute_script("document.querySelector('body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > div.form-group > div.c-custom-field > input').value='test@gmail.com'")
    driver.execute_script("document.querySelector('#firstName').value='test'")
    driver.execute_script("document.querySelector('#lastName').value='test'")
    driver.execute_script("document.querySelector('#address1').value='test'")
    driver.execute_script("document.querySelector('#address2').value='test'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pcode = driver.find_element_by_id("postalCode")
    pcode.send_keys("W13 3BG")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='123123123'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
    paypp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[4]/div/label/div[2]/div/div/iframe")
    driver.switch_to.frame(paypp)
    time.sleep(4)


    driver.execute_script("document.querySelector('.paypal-button-label-container').click()")

    wait.until(EC.number_of_windows_to_be(2))


    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(10)        
    email = driver.find_element_by_id("email")
    email.send_keys("johann_1317033282_per@finntack.com")

    execute_qs(driver, "#btnNext")
    time.sleep(4)

    pswrd = driver.find_element_by_id("password")
    pswrd.send_keys("123qweasd")   

    execute_qs(driver, "#btnLogin")
    time.sleep(10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    execute_qs(driver, "#consentButton")

    driver.switch_to.window(original_window)
    
    # time.sleep(10)
    # execute_qs(driver, "body > div.container.my-60 > div > div.col-12.col-md-8 > div.row.justify-content-center.justify-content-sm-between.mt-30.mb-15 > div > a")
    time.sleep(8)

    result = driver.find_element_by_link_text("vos commandes")
    
    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()



def test_FR_order_CC():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)

    driver.get("https://storefront:horze123@hrzfr.sta.horze.io/pantalon-dequitation-grip---femme/pantalon-dequitation-taille-haute-horze-tara-silicone-fond-integral-femme/36091.html#color=VDB")

    driver.maximize_window()

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # select size
    execute_qs(driver, "#size-select")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(1)")      
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    time.sleep(4)
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(5)
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div.bg-white.p-15.p-sm-30.mb-sm-30 > div > div > div > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div:nth-child(3) > a")
    time.sleep(3)
    driver.execute_script("document.querySelector('body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > div.form-group > div.c-custom-field > input').value='test@gmail.com'")
    driver.execute_script("document.querySelector('#firstName').value='test'")
    driver.execute_script("document.querySelector('#lastName').value='test'")
    driver.execute_script("document.querySelector('#address1').value='test'")
    driver.execute_script("document.querySelector('#address2').value='test'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pcode = driver.find_element_by_id("postalCode")
    pcode.send_keys("W13 3BG")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='123123123'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.offset-lg-1.mb-15 > div:nth-child(2) > label")
    time.sleep(3)

    name = driver.find_element_by_id("braintreeCardOwner")
    name.send_keys("test test")

    time.sleep(4)
    ele = driver.find_element_by_xpath("//*[@id='braintree-hosted-field-number']")

    driver.switch_to.frame(ele)
    time.sleep(3)

    cardnumber = driver.find_element_by_id("credit-card-number")
    cardnumber.send_keys("4111 1111 1111 1111")
    time.sleep(3)
    driver.switch_to.default_content()
    time.sleep(4)
    ele1 = driver.find_element_by_xpath("//*[@id='braintree-hosted-field-expirationDate']")
    driver.switch_to.frame(ele1)
    time.sleep(4)
    expiration = driver.find_element_by_id("expiration")
    expiration.send_keys("12/25")
    driver.switch_to.default_content()
    ele2 = driver.find_element_by_xpath("//*[@id='braintree-hosted-field-cvv']")
    driver.switch_to.frame(ele2)
    time.sleep(4)
    cvc = driver.find_element_by_id("cvv")
    cvc.send_keys("123")
    driver.switch_to.default_content()
    time.sleep(4)

    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div.row.payment-method-fragment-js > div.col-12.col-sm-6.col-lg-4.c-totals.c-totals--float.floating-totals-js.offset-sm-6.mb-15.px-0 > div > label > a")
    

    time.sleep(10)
    result = driver.find_element_by_link_text("vos commandes")

    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()  



def test_NL_order_iDEAL():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)

    driver.get("https://storefront:horze123@hrznl.sta.horze.io/dames-full-seat-rijbroeken/horze-active-siliconen-grip-full-seat-rijbroek-dames/36277.html#color=BL")
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    time.sleep(5)
    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # select size
    execute_qs(driver, "#size-select > div")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(1)")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    time.sleep(4)
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    # insert email
    driver.execute_script("document.querySelector(scrollTo(0, 500))")
    time.sleep(4)
    email = driver.find_element_by_id("email")
    email.send_keys("pawel.sikora@rocksoft.pl")

    time.sleep(5)

    execute_qs(driver, "body > div.container > div > div.col-lg-9 > div.step-wrapper.step-5 > div:nth-child(2) > ul > li:nth-child(2) > a")

    driver.execute_script("document.querySelector(scrollTo(0, 1900))")
    time.sleep(4)

    execute_qs(driver, "body > div.container > div > div.col-lg-9 > div.step-wrapper.step-5 > div:nth-child(2) > ul > li:nth-child(4) > a")
    time.sleep(5)

    firstname = driver.find_element_by_name("billing-firstName")
    firstname.send_keys("pawel")

    lastname = driver.find_element_by_id("billing-lastName")
    lastname.send_keys("Sikora")

    address1 = driver.find_element_by_id("billing-address1")
    address1.send_keys("test")

    housenr = driver.find_element_by_id("billing-suite")
    housenr.send_keys("12")

    address2 = driver.find_element_by_id("billing-address2")
    address2.send_keys("test")

    city = driver.find_element_by_id("billing-city")
    city.send_keys("test")

    postcode = driver.find_element_by_id("billing-postalCode")
    postcode.send_keys("2521VA")

    pnumber = driver.find_element_by_id("billing-phone")
    pnumber.send_keys("0612345678")

    driver.find_element_by_id("tac").click()

    time.sleep(5)
    driver.find_element_by_id("checkout-localPayments-js").click()

    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


    element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "successSubmit")))        
    
    element.click()

    time.sleep(10)

    driver.switch_to.window(original_window)

    time.sleep(70)

    result = driver.find_element_by_link_text("Horze Active Siliconen Grip Full Seat Rijbroek, dames")

    assert result.is_displayed() == True

    time.sleep(4)

    driver.close()



def test_CH_order_klarna():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)

    driver.get("https://storefront:horze123@hrzch.sta.horze.io/vollbesatzreithosen-fuer-damen/horze-active-damen-vollbesatzreithose-mit-silikon-grip/36277.html")

    driver.maximize_window()

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # select size
    execute_qs(driver, "#size-select > div")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(1)")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(5)
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div.bg-white.p-15.p-sm-30.mb-sm-30 > div > div > div > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div:nth-child(3) > a")
    time.sleep(3)
    driver.execute_script("document.querySelector('body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > div.form-group > div.c-custom-field > input').value='test@gmail.com'")
    driver.execute_script("document.querySelector('#firstName').value='test'")
    driver.execute_script("document.querySelector('#lastName').value='test'")
    driver.execute_script("document.querySelector('#address1').value='test'")
    driver.execute_script("document.querySelector('#address2').value='test'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pcode = driver.find_element_by_id("postalCode")
    pcode.send_keys("1234")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='41242424444'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)   


    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div.row.payment-method-fragment-js > div.col-12.col-sm-6.col-lg-4.c-totals.c-totals--float.floating-totals-js.offset-sm-6.mb-15.px-0 > div > label > a")


    time.sleep(10)
    result = driver.find_element_by_link_text("Horze Durable Saddle Rack")

    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()



def test_HU_order_PayPal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzhu.sta.horze.io/egyeb-etrendkiegeszítok-lovaknak/trikem-vimital-zinc-500g/323922.html")

    driver.maximize_window()

    time.sleep(5)
    
    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1
    time.sleep(4)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # change color

    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    time.sleep(3)
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(5)
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div.bg-white.p-15.p-sm-30.mb-sm-30 > div > div > div > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div:nth-child(3) > a")
    time.sleep(3)
    driver.execute_script("document.querySelector('body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > div.form-group > div.c-custom-field > input').value='test@gmail.com'")
    driver.execute_script("document.querySelector('#firstName').value='test'")
    driver.execute_script("document.querySelector('#lastName').value='test'")
    driver.execute_script("document.querySelector('#address1').value='test'")
    driver.execute_script("document.querySelector('#address2').value='test'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pcode = driver.find_element_by_id("postalCode")
    pcode.send_keys("W13 3BG")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='123123123'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.offset-lg-1.mb-15 > div:nth-child(2) > label")
    time.sleep(3)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
    paypp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[4]/div/label/div[2]/div/div/iframe")
    driver.switch_to.frame(paypp)
    time.sleep(4)


    driver.execute_script("document.querySelector('.paypal-button-label-container').click()")

    wait.until(EC.number_of_windows_to_be(2))


    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(10)        
    email = driver.find_element_by_id("email")
    email.send_keys("johann_1317033282_per@finntack.com")

    execute_qs(driver, "#btnNext")
    time.sleep(4)

    pswrd = driver.find_element_by_id("password")
    pswrd.send_keys("123qweasd")   

    execute_qs(driver, "#btnLogin")
    time.sleep(10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    execute_qs(driver, "#consentButton")

    driver.switch_to.window(original_window)
    
    time.sleep(10)
    result = driver.find_element_by_link_text("Rendelései menüpontban")

    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()     



def test_ES_order_PayPal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzes.sta.horze.io/capas-base-mujer/camisa-de-mangas-cortas-funcional-para-mujer-horze-mathilde/33522.html#color=MSBE")

    driver.maximize_window()

    time.sleep(5)
    
    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1
    time.sleep(4)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # choose size
    
    execute_qs(driver, "#size-select > div")

    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(2)")

    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div > div > div > div > div:nth-child(2) > div > div > div > label")
    
    time.sleep(4)

    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    time.sleep(3)
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(5)
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div.bg-white.p-15.p-sm-30.mb-sm-30 > div > div > div > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div:nth-child(3) > a")
    time.sleep(3)
    driver.execute_script("document.querySelector('body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > div.form-group > div.c-custom-field > input').value='test@gmail.com'")
    driver.execute_script("document.querySelector('#firstName').value='test'")
    driver.execute_script("document.querySelector('#lastName').value='test'")
    driver.execute_script("document.querySelector('#address1').value='test'")
    driver.execute_script("document.querySelector('#address2').value='test'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pcode = driver.find_element_by_id("postalCode")
    pcode.send_keys("W13 3BG")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='123123123'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
    paypp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[4]/div/label/div[2]/div/div/iframe")
    driver.switch_to.frame(paypp)
    time.sleep(4)


    driver.execute_script("document.querySelector('.paypal-button-label-container').click()")

    wait.until(EC.number_of_windows_to_be(2))


    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(10)        
    email = driver.find_element_by_id("email")
    email.send_keys("johann_1317033282_per@finntack.com")

    execute_qs(driver, "#btnNext")
    time.sleep(4)

    pswrd = driver.find_element_by_id("password")
    pswrd.send_keys("123qweasd")   

    execute_qs(driver, "#btnLogin")
    time.sleep(10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    execute_qs(driver, "#consentButton")

    driver.switch_to.window(original_window)

    time.sleep(10)
    result = driver.find_element_by_link_text("Tus pedidos")

    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()   

