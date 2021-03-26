import time
from selenium import webdriver
import pytest
import json
from endpoint.EndPointFactory import EndPoint, Flipkart, Amazon


@pytest.fixture(scope='session')
def config():
    with open(r'C:\Users\chiragm\PycharmProjects\TopDocProject\feature\config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture()
def test_setup(config):
    global driver

    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--disable-gpu')

    if config['browser'] == 'chrome':
        driver = webdriver.Chrome(r'C:\Users\chiragm\PycharmProjects\TopDocProject\drivers\chromedriver.exe')


    driver.implicitly_wait(config['wait_time'])
    driver.maximize_window()
    driver.get(EndPoint.BASE_URI_UI)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(config['wait_time'])

    yield
    time.sleep(1)
    driver.quit()


def test_flipkart(test_setup):
    driver.find_element_by_xpath(Flipkart.LoginPopupCancel).click()
    driver.find_element_by_xpath(Flipkart.SearchTextBox).send_keys(EndPoint.ProductSearch)
    driver.find_element_by_xpath(Flipkart.SearchButton).click()
    driver.find_element_by_xpath(Flipkart.ProductLink).click()
    driver.switch_to.window(driver.window_handles[1])
    price = driver.find_element_by_xpath(Flipkart.ProductPrice).text
    print("\nPrice of the product in Flipkart is: ",price)
    driver.find_element_by_xpath(Flipkart.AddToCartButton).click()
    driver.implicitly_wait(10)
    time.sleep(5)
    #element = driver.find_element_by_xpath(Flipkart.CartAddQuantity)
    #webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    driver.find_element_by_xpath(Flipkart.CartAddQuantity).click()
    time.sleep(3)
    totalprice = driver.find_element_by_xpath(Flipkart.CartTotalPrice).text
    print("Total Cart value of Flipkart is: ",totalprice)

def test_amazon(test_setup):
    driver.find_element_by_xpath(Flipkart.LoginPopupCancel).click()
    driver.find_element_by_xpath(Flipkart.SearchTextBox).send_keys(EndPoint.ProductSearch)
    driver.find_element_by_xpath(Flipkart.SearchButton).click()
    driver.find_element_by_xpath(Flipkart.ProductLink).click()
    driver.switch_to.window(driver.window_handles[1])
    price = driver.find_element_by_xpath(Flipkart.ProductPrice).text
    print("\nPrice of the Product in Flipkart is: ",price)
    driver.find_element_by_xpath(Flipkart.AddToCartButton).click()
    driver.implicitly_wait(10)
    time.sleep(3)
    totalprice = driver.find_element_by_xpath(Flipkart.CartTotalPrice).text
    print("Total Cart Value in Flipkart is: ",totalprice)

    driver.execute_script("window.open('https://www.amazon.in/')")
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element_by_xpath(Amazon.SearchTextBox).send_keys(EndPoint.ProductSearch)
    driver.find_element_by_xpath(Amazon.SearchButton).click()
    driver.find_element_by_xpath(Amazon.ProductLink).click()
    driver.switch_to.window(driver.window_handles[3])
    driver.implicitly_wait(10)
    price2 = driver.find_element_by_xpath(Amazon.ProductPrice).text
    print("Price of the product in Amazon is:",price2)
    driver.find_element_by_xpath(Amazon.AddToCartButton).click()
    driver.implicitly_wait(10)
    time.sleep(3)
    totalprice2 = driver.find_element_by_xpath(Amazon.CartTotalPrice).text
    print("Total cart value in Amazon is:",totalprice2)
    if totalprice > totalprice2:
        print("Amazon gives cheaper product")
    elif totalprice == totalprice2:
        print("Both amazon and flipkart has same price")
    else:
        print("Flipkart gives cheaper product")
