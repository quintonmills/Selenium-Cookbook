from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class login():
    def dialog(self):
        driver = webdriver.Chrome(executable_path="/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver")
        baseURL = "https://www.jqueryui.com"
        driver.get(baseURL)
        menuSelect = driver.find_element(By. XPATH, "//*[@id='sidebar']/aside[2]/ul/li[8]/a")
        menuSelect.click()
        iframe = driver.find_element(By. XPATH, '//*[@id="content"]/iframe')
        driver.switch_to_frame(iframe)
        menuBooks = driver.find_element(By. XPATH, '//*[@id="ui-id-2"]')
        menuBooks.click()
        time.sleep(2)
ff=login()
ff.dialog()