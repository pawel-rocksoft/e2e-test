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

def test_DE_order_klarna():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)

    driver.get("https://storefront:horze123@hrzde.sta.horze.io/vollbesatzreithosen-fuer-damen/horze-active-damen-vollbesatzreithose-mit-silikon-grip/36277.html")

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
    # pay with klarna
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div:nth-child(1) > div > div > div > a.btn.btn-black.w-100.start-checkout-js")
    # as a guest
    execute_qs(driver, "#loginForm > div > div > div.modal-body.px-sm-30.px-md-30.pb-sm-30.pb-md-60.pt-0 > div > div.col-12.col-sm.pb-60.pb-sm-0 > a")
 
    time.sleep(5)

    driver.switch_to.frame("klarna-checkout-iframe")

    billingadress = driver.find_element_by_id("billing-email")

    billingadress.send_keys("pawel.sikora@rocksoft.pl")

    postcode = driver.find_element_by_id("billing-postal_code")

    postcode.send_keys("41460")
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    driver.find_element_by_id("billing-title").click()
    time.sleep(2)
    driver.find_element_by_id("billing-title__option__herr").click()

    address = driver.find_element_by_id("billing-street_address")
    address.send_keys("test 43")

    postcode.send_keys(Keys.RETURN)
    time.sleep(3)
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    driver.switch_to.default_content()

    driver.execute_script("window.scrollTo(20, document.body.scrollHeight)")
    time.sleep(4)
    driver.switch_to.frame("klarna-checkout-iframe")
    time.sleep(3)
    

    buy = "document.querySelector('#page > div > div:nth-child(2) > div > div > div:nth-child(11) > div > button > div > div:nth-child(1)').click()"

    driver.execute_script(buy)

    # driver.find_element_by_xpath("//*[@id='page']/div/div[2]/div/div/div[7]/div/button/div/div[2]/span").click()

    # driver.switch_to.default_content()

    time.sleep(4)

    driver.switch_to.frame("klarna-checkout-iframe")

    time.sleep(4)

    result = driver.find_element_by_id("section-header__content")

    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()



def test_DE_order_amazon():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)


    driver.get("https://storefront:horze123@hrzde.sta.horze.io/sattelkammer-zubehoer/horze-stabiler-sattelhalter/50000.html")

    driver.maximize_window()

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    
    # change color
    # execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div > div > div > div > div:nth-child(2)")
    
    # driver.find_element_by_class_name("c-color-swatch color-swatch-js color-label-js").click()

    # add to cart

    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    # pay with amazon
    amazon = "document.querySelector('body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div:nth-child(1) > div > div > div > label:nth-child(5) > div').click()"
    driver.execute_script(amazon)

    time.sleep(5)

    email = driver.find_element_by_id("ap_email")
    email.send_keys("pawel.sikora@horze.com")

    time.sleep(2)

    password = driver.find_element_by_id("ap_password")
    password.send_keys(")v)NwWNM?8pq@bT")

    execute_qs(driver, "#signInSubmit")

    time.sleep(5)

    execute_qs(driver, "#change-address-button")

    time.sleep(5)

    execute_qs(driver, "#selection-heading > ul > div > span > li:nth-child(2)")

    time.sleep(3)

    execute_qs(driver, "#a-autoid-2 > span > input")

    time.sleep(5)


    execute_qs(driver, "#a-autoid-6 > span > input")
    #a-autoid-0 > span > input
    time.sleep(5)

    execute_qs(driver, "body > div.container.my-60 > div > div.col-12.col-md-8 > div.row.justify-content-center.justify-content-sm-between.mt-30.mb-15 > div > a")
    
    time.sleep(10)

    result = driver.find_element_by_link_text("Meine Bestellung ansehen")
    
    assert result.is_displayed() == True


    time.sleep(9)
    driver.close()



def test_DE_order_klarna_paypal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzde.sta.horze.io/vollbesatzreithosen-fuer-damen/horze-active-damen-vollbesatzreithose-mit-silikon-grip/36277.html")

    driver.maximize_window()

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
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    # pay with klarna
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div:nth-child(1) > div > div > div > a.btn.btn-black.w-100.start-checkout-js")
    # as a guest
    execute_qs(driver, "#loginForm > div > div > div.modal-body.px-sm-30.px-md-30.pb-sm-30.pb-md-60.pt-0 > div > div.col-12.col-sm.pb-60.pb-sm-0 > a")
 
    time.sleep(5)

    driver.switch_to.frame("klarna-checkout-iframe")

    billingadress = driver.find_element_by_id("billing-email")

    billingadress.send_keys("pawel.sikora@rocksoft.pl")

    postcode = driver.find_element_by_id("billing-postal_code")

    postcode.send_keys("41460")
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    driver.find_element_by_id("billing-title").click()
    time.sleep(2)
    driver.find_element_by_id("billing-title__option__herr").click()

    address = driver.find_element_by_id("billing-street_address")
    address.send_keys("test 43")

    postcode.send_keys(Keys.RETURN)
    time.sleep(3)
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    driver.switch_to.default_content()

    driver.execute_script("window.scrollTo(20, document.body.scrollHeight)")
    time.sleep(4)
    driver.switch_to.frame("klarna-checkout-iframe")
    time.sleep(3)

    driver.execute_script("document.querySelector('#payment-selector-external_paypal__label').click()")

    time.sleep(4)
    pejpal1 = "document.querySelector('#page > div > div:nth-child(2) > div > div > div:nth-child(11) > div > button > div > div:nth-child(1)').click()"
    driver.execute_script(pejpal1)

    time.sleep(7)

    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[1]").click()

    driver.execute_script("$('.paypal-button').click()")
    
    driver.execute_script("console.log($('[data-button]'))")
    driver.execute_script("$('[data-button]').click()")

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

    result = driver.find_element_by_link_text("Meine Bestellung ansehen")
    
    assert result.is_displayed() == True

    time.sleep(5)
    driver.close()



def test_DE_order_paypal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzde.sta.horze.io/vollbesatzreithosen-fuer-damen/horze-active-damen-vollbesatzreithose-mit-silikon-grip/36277.html")

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
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(4)
    FR = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div/label[1]/div/div/div/iframe")
    driver.switch_to.frame(FR)
    PP = "document.querySelector('#paypal-animation-content > div.paypal-button-container.paypal-button-layout-vertical.paypal-button-shape-rect.paypal-button-branding-branded.paypal-button-number-single.paypal-button-env-sandbox.paypal-should-focus > div > div > img.paypal-button-logo.paypal-button-logo-paypal.paypal-button-logo-gold').click()"
    driver.execute_script(PP)

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
    execute_qs(driver, "body > div.container.my-60 > div > div.col-12.col-md-8 > div.row.justify-content-center.justify-content-sm-between.mt-30.mb-15 > div > a")
    time.sleep(8)

    result = driver.find_element_by_link_text("Meine Bestellung ansehen")
    
    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()



def test_NO_order_klarna_paylater():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)

    driver.get("https://storefront:horze123@www.hrzno.sta.horze.io/allround--sprangsjabraker/horze-chooze-allround-sjabrak/17000.html")

    driver.maximize_window()

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    # select size
    execute_qs(driver, "#size-select")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(1)")
    # add to cart       
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    # go to checkout    
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    # pay with klarna
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div:nth-child(1) > div > div > div > a.btn.btn-black.w-100.start-checkout-js")
    # as a guest
    execute_qs(driver, "#loginForm > div > div > div.modal-body.px-sm-30.px-md-30.pb-sm-30.pb-md-60.pt-0 > div > div.col-12.col-sm.pb-60.pb-sm-0 > a")

    time.sleep(5)

    driver.switch_to.frame("klarna-checkout-iframe")

    billingadress = driver.find_element_by_id("billing-email")
    billingadress.send_keys("pawel.sikora@rocksoft.pl")

    postcode = driver.find_element_by_id("billing-postal_code")
    postcode.send_keys("4160")

    postcode.send_keys(Keys.RETURN)

    time.sleep(5)

    name = driver.find_element_by_id("billing-given_name")
    name.send_keys("Pawel")

    sourname = driver.find_element_by_id("billing-family_name")
    sourname.send_keys("Sikora")

    # address = driver.find_element_by_id("billing-street_address")
    # address.send_keys("Sæffleberggate 56")

    mobilephone = driver.find_element_by_id("billing-phone")
    mobilephone.send_keys("40 123 456")

    mobilephone.send_keys(Keys.RETURN)
    time.sleep(3)
    mobilephone.send_keys(Keys.RETURN)

    time.sleep(4)

    driver.switch_to.default_content()
    time.sleep(2)

    driver.execute_script("window.scrollTo(20, document.body.scrollHeight)")
    time.sleep(4)
    driver.switch_to.frame("klarna-checkout-iframe")
    time.sleep(3)

    buy = "document.querySelector('#page > div > div:nth-child(2) > div > div > div:nth-child(9) > div > button > div > div:nth-child(1)').click()"
    driver.execute_script(buy)

    driver.switch_to.default_content()

    time.sleep(4)

    driver.switch_to.frame("klarna-fullscreen-iframe")

    personalnumber = driver.find_element_by_id("nin")
    personalnumber.send_keys("01087000571")

    proceed = "document.querySelector('#supplement_nin_dialog__footer-button-wrapper > div > button').click()"
    driver.execute_script(proceed)
    driver.switch_to.default_content()

    time.sleep(5)

    driver.switch_to.frame("klarna-checkout-iframe")

    time.sleep(5)

    result = driver.find_element_by_id("section-header__content")

    assert result.is_displayed() == True

    driver.close()




def test_NO_order_paypal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@www.hrzno.sta.horze.io/helforsterkede-ridebukser-til-dame/horze-active-helforsterket-dameridebukse-med-silikon/36277.html")

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
    execute_qs(driver, "#size-select")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(1)")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div:nth-child(1) > div > div > div > a.btn.btn-black.w-100.start-checkout-js")
    # as a guest
    execute_qs(driver, "#loginForm > div > div > div.modal-body.px-sm-30.px-md-30.pb-sm-30.pb-md-60.pt-0 > div > div.col-12.col-sm.pb-60.pb-sm-0 > a")
 
    time.sleep(5)

    driver.switch_to.frame("klarna-checkout-iframe")

    billingadress = driver.find_element_by_id("billing-email")

    billingadress.send_keys("pawel.sikora@rocksoft.pl")

    postcode = driver.find_element_by_id("billing-postal_code")

    postcode.send_keys("4146")
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    address = driver.find_element_by_id("billing-street_address")
    address.send_keys("test 43")
    time.sleep(5)

    address.send_keys(Keys.RETURN)
    time.sleep(5)
    address.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.switch_to.default_content()

    driver.execute_script("scrollTo(0, document.body.scrollHeight)")
    time.sleep(4)
    driver.switch_to.frame("klarna-checkout-iframe")
    time.sleep(3)
    execute_qs(driver, "#payment-selector-external_paypal")
    time.sleep(5)

    buy = "document.querySelector('#page > div > div:nth-child(2) > div > div > div:nth-child(9) > div > button > div > div:nth-child(1)').click()"

    driver.execute_script(buy) 

    time.sleep(10)

    # paypal = "document.querySelector('#paypal-animation-content > div.paypal-button-container.paypal-button-layout-vertical.paypal-button-shape-rect.paypal-button-branding-branded.paypal-button-number-single.paypal-button-env-sandbox.paypal-should-focus > div').click()"

    # driver.execute_script(paypal) 
   
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[1]").click()

    driver.execute_script("$('.paypal-button').click()")
    
    driver.execute_script("console.log($('[data-button]'))")
    driver.execute_script("$('[data-button]').click()")
    
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

    driver.find_element_by_id("consentButton").click()


    time.sleep(10)
    # driver.switch_to.default_content()
    driver.switch_to.window(original_window)
    time.sleep(5)
    result = driver.find_element_by_link_text("Vis min bestilling")
    
    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()



def test_FI_order_klarna():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)

    driver.get("https://storefront:horze123@hrzfi.sta.horze.io/hevostarvikkeet-ratsastustarvikkeet---horze.fi/horze-gift-card/98000.html")

    driver.maximize_window()

    time.sleep(4)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    
    email = driver.find_element_by_id("giftcard-to-email")
    email.send_keys("pawel.sikora@rocksoft.pl")

    name = driver.find_element_by_id("giftcard-to-name")
    name.send_keys("test")

    subject = driver.find_element_by_id("giftcard-subject")
    subject.send_keys("test")

    fromm = driver.find_element_by_id("giftcard-from")
    fromm.send_keys("test")

    message = driver.find_element_by_id("giftcard-message")
    message.send_keys("test")

    time.sleep(3)

    execute_qs(driver, "body > div.mb-40 > div.container.pt-5 > div > div.col-12.col-sm-5.px-0.px-sm-15 > form > div.c-giftcard-design__form.mt-15.px-15.px-sm-0 > div > div.row.justify-content-end.m-0 > div > button")

    # pay with klarna
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div > div > div > div > a.btn.btn-black.w-100.start-checkout-js")
    # as a guest
    execute_qs(driver, "#loginForm > div > div > div.modal-body.px-sm-30.px-md-30.pb-sm-30.pb-md-60.pt-0 > div > div.col-12.col-sm.pb-60.pb-sm-0 > a")

    time.sleep(5)

    driver.switch_to.frame("klarna-checkout-iframe")

    billingadress = driver.find_element_by_id("billing-email")

    billingadress.send_keys("pawel.sikora@rocksoft.pl")

    postcode = driver.find_element_by_id("billing-postal_code")

    postcode.send_keys("41460")
    postcode.send_keys(Keys.RETURN)

    time.sleep(4)

    name = driver.find_element_by_id("billing-given_name")
    name.send_keys("test")

    famname = driver.find_element_by_id("billing-family_name")
    famname.send_keys("test")

    address = driver.find_element_by_id("billing-street_address")
    address.send_keys("Sæffleberggate 56")

    city = driver.find_element_by_id("billing-city")
    city.send_keys("Helsinki")

    mobilephone = driver.find_element_by_id("billing-phone")
    mobilephone.send_keys("03 43434")

    city.send_keys(Keys.RETURN)
    time.sleep(4)
    city.send_keys(Keys.RETURN)

    driver.switch_to.default_content()
    time.sleep(2)

    driver.execute_script("window.scrollTo(20, document.body.scrollHeight)")
    time.sleep(4)
    driver.switch_to.frame("klarna-checkout-iframe")
    time.sleep(3)

    buy = "document.querySelector('#page > div > div:nth-child(2) > div > div > div:nth-child(9) > div > button > div > div:nth-child(1)').click()"

    driver.execute_script(buy)

    driver.switch_to.default_content()

    time.sleep(5)

    driver.switch_to.frame("klarna-fullscreen-iframe")
    time.sleep(5)

    personalnumber = driver.find_element_by_id("nin")
    personalnumber.send_keys("190122-829F")

    proceed = "document.querySelector('#supplement_nin_dialog__footer-button-wrapper > div > button > div > div:nth-child(1)').click()"
    driver.execute_script(proceed)
    driver.switch_to.default_content()

    time.sleep(4)

    driver.switch_to.frame("klarna-checkout-iframe")

    time.sleep(4)

    result = driver.find_element_by_id("section-header__content")

    assert result.is_displayed() == True

    time.sleep(4)

    driver.close()




def test_FI_order_paypal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzfi.sta.horze.io/naisten-ratsastushousut-kokopaikoilla/horze-active--naisten-ratsastushousut-silikonipainatetuilla-kokopaikoilla/36277.html")

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
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(4)
    # pay with klarna
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div:nth-child(1) > div > div > div > a.btn.btn-black.w-100.start-checkout-js")
    # as a guest
    execute_qs(driver, "#loginForm > div > div > div.modal-body.px-sm-30.px-md-30.pb-sm-30.pb-md-60.pt-0 > div > div.col-12.col-sm.pb-60.pb-sm-0 > a")
 
    time.sleep(5)

    driver.switch_to.frame("klarna-checkout-iframe")

    billingadress = driver.find_element_by_id("billing-email")

    billingadress.send_keys("pawel.sikora@rocksoft.pl")

    postcode = driver.find_element_by_id("billing-postal_code")

    postcode.send_keys("41460")
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    # driver.find_element_by_id("billing-title").click()
    # time.sleep(2)
    # driver.find_element_by_id("billing-title__option__herr").click()

    # address = driver.find_element_by_id("billing-street_address")
    # address.send_keys("test 43")

    postcode.send_keys(Keys.RETURN)
    time.sleep(3)
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    driver.switch_to.default_content()

    driver.execute_script("window.scrollTo(20, document.body.scrollHeight)")
    time.sleep(4)
    driver.switch_to.frame("klarna-checkout-iframe")
    time.sleep(3)

    driver.execute_script("document.querySelector('#payment-selector-external_paypal__label').click()")

    time.sleep(4)
    pejpal1 = "document.querySelector('#page > div > div:nth-child(2) > div > div > div:nth-child(9) > div > button > div > div:nth-child(1)').click()"
    driver.execute_script(pejpal1)

    time.sleep(10)

    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[1]").click()

    driver.execute_script("$('.paypal-button').click()")
    
    driver.execute_script("console.log($('[data-button]'))")
    driver.execute_script("$('[data-button]').click()")

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

    result = driver.find_element_by_link_text("Katso tilauksen tiedot")
    
    assert result.is_displayed() == True

    time.sleep(5)
    driver.close()



def test_AT_order_klarna():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    

    driver.get("https://storefront:horze123@hrzat.sta.horze.io/andere-ergaenzungen/trikem-vimital-zink-500g/323922.html")

    driver.maximize_window()

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    driver.execute_script(geopopup)
    
    # add to cart
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    # go to checkout
    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    time.sleep(4)
    # pay with klarna
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div:nth-child(1) > div > div > div > a")
    time.sleep(3)
    # logging in
    username = driver.find_element_by_name("username")
    username.send_keys("pawel.sikora@rocksoft.pl")
    time.sleep(4)

    password = driver.find_element_by_name("password")
    password.send_keys("Pawel12345^")
    time.sleep(4)

    execute_qs(driver, "#loginForm > div > div > div.modal-body.px-sm-30.px-md-30.pb-sm-30.pb-md-60.pt-0 > div > div.col-12.col-sm.offset-lg-1 > form > input.btn.btn-black.btn-block")

    time.sleep(5)

    driver.switch_to.frame("klarna-checkout-iframe")

    postcode = driver.find_element_by_id("billing-postal_code")

    postcode.send_keys("4146")
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    postcode.send_keys(Keys.RETURN)
    time.sleep(3)
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)
    driver.switch_to.default_content()
    time.sleep(2)

    driver.execute_script("window.scrollTo(20, document.body.scrollHeight)")
    time.sleep(4)
    driver.switch_to.frame("klarna-checkout-iframe")
    time.sleep(3)

    buy = "document.querySelector('#page > div > div:nth-child(2) > div > div > div:nth-child(11) > div > button > div > div:nth-child(1)').click()"

    driver.execute_script(buy)

    driver.switch_to.default_content()

    time.sleep(4)

    driver.switch_to.frame("klarna-checkout-iframe")

    time.sleep(4)

    result = driver.find_element_by_id("section-header__content")

    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()



def test_SE_order_paypal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://storefront:horze123@hrzse.sta.horze.io/helskodda-ridbyxor-foer-dam/horze-active-silikonhelskodda-damridbyxor/36277.html")

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
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div:nth-child(7) > div > div.col-12.show-on-color-available > div.c-dropdown__wrapper.dropdown.d-none.d-md-block.mb-15.dropdown-select-size-js.show > div.c-dropdown__menu.dropdown-menu.dropdown-menu-select-size-js.show > table > tr:nth-child(2)")
    execute_qs(driver, "body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15.product-instock-section-js > div.col.px-0 > button")
    # go to checkout
    # execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    # time.sleep(4)
    # FR = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div/label[1]/div/div/div/iframe")
    # driver.switch_to.frame(FR)
    # PP = "document.querySelector('#paypal-animation-content > div.paypal-button-container.paypal-button-layout-vertical.paypal-button-shape-rect.paypal-button-branding-branded.paypal-button-number-single.paypal-button-env-sandbox.paypal-should-focus > div > div > img.paypal-button-logo.paypal-button-logo-paypal.paypal-button-logo-gold').click()"
    # driver.execute_script(PP)

    execute_qs(driver, "body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a")
    execute_qs(driver, "body > div.l-cart__wrapper > div > div.mb-30.p-sm-30.bg-light > div > div.col-12.col-md-4.px-0.px-sm-15 > div > div:nth-child(1) > div > div > div > a.btn.btn-black.w-100.start-checkout-js")
    # as a guest
    execute_qs(driver, "#loginForm > div > div > div.modal-body.px-sm-30.px-md-30.pb-sm-30.pb-md-60.pt-0 > div > div.col-12.col-sm.pb-60.pb-sm-0 > a")
    time.sleep(5)
    driver.switch_to.frame("klarna-checkout-iframe")

    billingadress = driver.find_element_by_id("billing-email")

    billingadress.send_keys("pawel.sikora@rocksoft.pl")

    postcode = driver.find_element_by_id("billing-postal_code")

    postcode.send_keys("41466")
    postcode.send_keys(Keys.RETURN)
    time.sleep(4)

    address = driver.find_element_by_id("billing-given_name")
    address.send_keys("test 43")
    time.sleep(5)

    address0 = driver.find_element_by_id("billing-family_name")
    address0.send_keys("test 43")
    time.sleep(5)

    address7 = driver.find_element_by_id("billing-street_address")
    address7.send_keys("test 43")
    time.sleep(5)

    
    address5 = driver.find_element_by_id("billing-phone")
    address5.send_keys("0493-24 33 33")
    time.sleep(5)

    address.send_keys(Keys.RETURN)
    time.sleep(5)
    address.send_keys(Keys.RETURN)
    time.sleep(10)

    driver.switch_to.default_content()
    time.sleep(2)

    driver.execute_script("window.scrollTo(20, document.body.scrollHeight)")
    time.sleep(4)
    driver.switch_to.frame("klarna-checkout-iframe")

    pejpal = "document.querySelector('#payment-selector-external_paypal__label').click()"
    driver.execute_script(pejpal)
    time.sleep(4)
    pejpal1 = "document.querySelector('#page > div > div:nth-child(2) > div > div > div:nth-child(9) > div > button > div > div:nth-child(1)').click()"
    driver.execute_script(pejpal1)

    time.sleep(7)

    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[1]").click()

    driver.execute_script("$('.paypal-button').click()")
    
    driver.execute_script("console.log($('[data-button]'))")
    driver.execute_script("$('[data-button]').click()")

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

    result = driver.find_element_by_link_text("Visa min order")
    
    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()




# def test_B2BEU_order():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     print(dir_path)

#     options = Options()
#     options.add_argument('--allow-running-insecure-content')
#     options.add_argument('--ignore-certificate-errors')
#     driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
#     wait = WebDriverWait(driver, 10)

#     driver.get("https://storefront:horze123@b2beu.sta.horze.io/en_GB/overreach-boots/horze-probell-boots/19764.html")

#     driver.maximize_window()
#     time.sleep(5)

#     original_window = driver.current_window_handleP
#     assert len(driver.window_handles) == 1

#     acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
#     driver.execute_script(acceptUC)

#     time.sleep(5)

#     customerID = "document.querySelector('#dwfrm_login > div:nth-child(2) > input').value='222222'"
#     driver.execute_script(customerID)

#     password = "document.querySelector('#dwfrm_login > div:nth-child(3) > input').value='222222'"
#     driver.execute_script(password)

#     driver.execute_script("document.querySelector('#dwfrm_login > div.row.flex-column.form-group > div.col-4 > button').click()")

#     time.sleep(5)

#     search = "document.querySelector('body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-7 > div > form > input').value='19764'"
#     driver.execute_script(search)
#     time.sleep(4)
#     driver.execute_script("document.querySelector('body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-7 > div > form > button').click()")
                           
#     time.sleep(5)

#     driver.execute_script("document.querySelector('body > div.position-relative.pb-50.no-sidebar.product-grid-js > div > div > div > div.position-relative.px-15.px-sm-0.mb-60.product-list-ajax-js > div.row.loadmore-section-js > div > div > div > a > div > p.c-product-tile__info-name.c-product-tile__info-name--single-line.mb-0.font-fancy').click()")

#     time.sleep(5)

#     quantity = "document.querySelector('body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.px-0.px-sm-15.pt-10 > div.c-variation-table.px-0.px-sm-20.py-20.border-bottom > div.px-15.px-sm-0.pt-20.variation-table-js > div.variation-table-content-js > div:nth-child(1) > div.col-4.font-12.font-sm-13.px-0.px-sm-15 > div > div > div > input').value='1'"
#     driver.execute_script(quantity)

#     # driver.execute_script("document.querySelector('body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.px-0.px-sm-15.pt-10 > div.c-variation-table.px-0.px-sm-20.py-20.border-bottom > div.px-15.px-sm-0.pt-20.variation-table-js > div.variation-table-content-js > div:nth-child(1) > div.col-4.font-12.font-sm-13.px-0.px-sm-15 > div > div > div > span:nth-child(5) > button').click()")
#     time.sleep(3)
#     driver.execute_script("window.scrollTo(20, document.body.scrollHeight)")
#     time.sleep(2)
#     driver.execute_script("document.querySelector('body > div.container.product-container-js > div.row.mt-5.mb-15.mb-sm-30 > div.col-12.col-sm-6.col-md-5.product-content-js.pl-sm-15.pl-lg-30.mt-10.mt-sm-0 > form > div.col-12.d-flex.mt-15 > div > button').click()")
#     time.sleep(4)
#     driver.execute_script("window.scrollTo(document.body.scrollTop, 1)")
#     time.sleep(4)
#     driver.execute_script("document.querySelector('body > div.navigation-desktop-js > div.c-header.header-js > div.container.d-none.d-md-block.h-100 > div > div.col-3 > div > div.dropdown.shopping-header-dropdown-js > a').click()")








#     result = driver.find_element_by_link_text("Visa min order")
    
#     assert result.is_displayed() == True

#     time.sleep(5)

#     driver.close()






def test_EU_order_paypal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://storefront:horze123@hrzeu.sta.horze.io/womens-full-seat-breeches/horze-active-womens-silicone-grip-full-seat-breeches/36277.html")

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







def test_WW_order_paypal():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://storefront:horze123@hrzww.sta.horze.io/womens-full-seat-breeches/horze-active-womens-silicone-grip-full-seat-breeches/36277.html")

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

    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/form/div[5]/div[9]/label/select").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/form/div[5]/div[9]/label/select/option[119]").click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0)") 
    time.sleep(3)
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
    





def test_PL_order_P24():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\WebDrivers\\chromedriver.exe', options = options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://storefront:horze123@hrzpl.sta.horze.io/bryczesy-z-pelnym-lejem-damskie/bryczesy-damskie-z-pelnym-lejem-silikonowym-horze-active/36277.html")

    driver.maximize_window()

    time.sleep(5)

    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1

    time.sleep(5)

    acceptUC = "document.querySelector('#usercentrics-root').shadowRoot.querySelector('#focus-lock-id > div > div > div.sc-iktFfs.biTlrK > div > div > div.sc-fKFxtB.kSqpRu > div > button.sc-gsTEea.cfRmfK').click()"
    driver.execute_script(acceptUC)

    # geopopup = "document.querySelector('body > div.c-bottom-notification.py-15.geo-banner-js.in > div > div > div > a').click()"
    # driver.execute_script(geopopup)
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
    pcode.send_keys("43430")
    driver.execute_script("document.querySelector('#city').value='test'")
    driver.execute_script("document.querySelector('#phone').value='123123123'")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div > form > input")
    time.sleep(4)
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.shipping-method-options-js > label:nth-child(1) > label")
    time.sleep(3)

    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.mt-15.mt-sm-40 > a")
    time.sleep(4)

    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-5.offset-lg-1.mb-15 > div:nth-child(3) > label")
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div > div.col-12.col-sm-6.col-lg-4.mb-15 > div.c-totals.c-totals--float.floating-totals-js > div > label > button")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
    execute_qs(driver, "body > div:nth-child(6) > div.container.pt-30.pb-60 > div.row.payment-method-fragment-js > div.col-12.col-sm-6.col-lg-4.c-totals.c-totals--float.floating-totals-js.offset-sm-6.mb-15.px-0 > div > label > a")

    wait.until(EC.number_of_windows_to_be(2))


    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(10)     

    execute_qs(driver, "#successSubmit")
    

    driver.switch_to.window(original_window)
    
  
    time.sleep(10)

    result = driver.find_element_by_link_text("Terms")
    
    assert result.is_displayed() == True

    time.sleep(5)

    driver.close()