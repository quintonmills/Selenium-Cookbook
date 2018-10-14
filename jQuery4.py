from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
class login():

    def test(self):
        baseUrl = "http://jqueryui.com/"
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        menuSelection = driver.find_element(By. XPATH, "//a[contains(text(),'Button')]")
        menuSelection.click()
        driver.switch_to.frame(0)
        buttonSelection = driver.find_element(By. XPATH, '//body/div[1]')
        buttonSelection.click()
        time.sleep(2)
ff = login()
ff.test()
