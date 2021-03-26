import time
from selenium import webdriver
import pytest
import json
from endpoint.EndPointFactory import EndPoint
from selenium.webdriver.support.ui import Select



@pytest.fixture(scope='session')
def config():
    with open(r'C:\Users\chiragm\PycharmProjects\TopDocProject\feature\config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def test_setup(config):
    global driver

    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--disable-gpu')
    path = r'C:\Users\chiragm\PycharmProjects\TopDocProject\drivers\chromedriver.exe'

    #if config['browser'] == 'chrome':
    driver = webdriver.Chrome(r'C:\Users\chiragm\PycharmProjects\TopDocProject\drivers\chromedriver.exe')
        #driver = webdriver.Chrome(executable_path=path, options=chrome_opt)
    #elif config['browser'] == 'ie':
        #driver = webdriver.Ie(r'C:\Users\mindfire\PycharmProjects\TopDocAssignment\drivers\IEDriverServer.exe')
    #else:
        #raise Exception(f'"{config["browser"]}" is not a supported browser')

    driver.implicitly_wait(config['wait_time'])
    driver.maximize_window()
    driver.get(EndPoint.BASE_URI_UI)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(config['wait_time'])
    #time.sleep(7)

    yield
    time.sleep(1)
    driver.quit()


def ttest_window(test_setup):
    driver.find_element_by_xpath("//input[@id='txtName']").send_keys("chiragm")
    driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("Change!900")
    driver.find_element_by_xpath("//input[@id='btnLogin']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//a[@id='ucGPSMenu_hlnkNewStuffs']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath("//tbody/tr[2]/td[1]/a[1]").click()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_xpath("//body/form[@id='aspnetForm']/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()
    driver.find_element_by_xpath("//a[@id='ucGPSMenu_lnkLogout']").click()

def ttest_iframe(test_setup):
    driver.find_element_by_xpath("//input[@id='inputServer']").clear()
    driver.find_element_by_xpath("//input[@id='inputServer']").send_keys("vavpr-ssosrv-01.curaspan.local")
    driver.find_element_by_xpath("//input[@id='loadPresetData']").click()
    driver.find_element_by_xpath("//body/div[1]/form[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/input[1]").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath("//body/div[1]/div[3]/form[2]/input[5]").click()
    driver.implicitly_wait(10)
    driver.switch_to.frame("ssoIframe")
    #driver.find_element_by_id("btn_cancel_referral").is_enabled()
    driver.switch_to.default_content()

def test_alert(test_setup):
    time.sleep(5)
    driver.implicitly_wait(5)
    data = driver.switch_to.alert
    print(data.text)
    data.send_keys("dev")
    data.accept()
    data.dismiss()





