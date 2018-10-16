from selenium import webdriver

from selenium.webdriver.common.by import By
import time
class login():
    def test(self):
        #accordation recipe
        baseURL = "https://www.jQueryui.com"
        driver = webdriver.Chrome("/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver")
        driver.get(baseURL)
        menuSelect = driver.find_element(By. XPATH, "//*[@id='sidebar']/aside[2]/ul/li[1]/a")
        menuSelect.click()
        time.sleep(3)
        iframe = driver.find_element(By. XPATH, '//*[@id="content"]/iframe')
        driver.switch_to_frame(iframe)
        section1 = driver.find_element(By. XPATH, '//*[@id="ui-id-1"]')
        section1.click() 
        time.sleep(1)
        section2 = driver.find_element(By. XPATH, '//*[@id="ui-id-3"]')
        section2.click()
        time.sleep(1)
ff=login()
ff.test()
