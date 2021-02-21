import time
from selenium import webdriver
import pytest
import json
from selenium.webdriver.support.ui import Select
from endpoint.EndPointFactory import EndPoint


@pytest.fixture(scope='session')
def config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def test_setup(config):
    global driver

    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--disable-gpu')
    path = r'C:\Users\mindfire\PycharmProjects\TopDocAssignment\drivers\chromedriver.exe'

    if config['browser'] == 'chrome':
        driver = webdriver.Chrome(executable_path=path, options=chrome_opt)
        #driver = webdriver.Chrome(r'C:\Users\mindfire\PycharmProjects\TopDocAssignment\drivers\chromedriver.exe')
    elif config['browser'] == 'ie':
        driver = webdriver.Ie(r'C:\Users\mindfire\PycharmProjects\TopDocAssignment\drivers\IEDriverServer.exe')
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')

    driver.implicitly_wait(config['wait_time'])
    driver.maximize_window()
    driver.get(EndPoint.BASE_URI_UI)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(config['wait_time'])
    time.sleep(7)

    yield
    time.sleep(1)
    driver.quit()


def test_signup(test_setup):
    driver.find_element_by_xpath("//app-education-header/nav[2]/div[1]/div[3]/figure[1]/img[1]").click()
    driver.find_element_by_xpath("/html/body/app-root/app-education-landing/app-education-header/nav[2]/div/div[3]/div/div[1]/div[2]/a").click()
    driver.implicitly_wait(10)
    data = driver.find_element_by_xpath("//body/app-root[1]/app-join-community[1]/main[1]/section[1]/div[1]/button[2]")
    print("\n",data.text)
