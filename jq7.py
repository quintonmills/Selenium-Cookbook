from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class login():
    #select menue recipe
    def test(self):
        driver = webdriver.Chrome(executable_path = "/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver")
        baseUrl = "https://www.jQueryui.com"
        driver.get(baseUrl)
        driver.maximize_window()
        menuSelect = driver.find_element(By. XPATH, '//*[@id="sidebar"]/aside[2]/ul/li[10]/a')
        menuSelect.click()
        iframe = driver.find_element(By. XPATH, '//*[@id="content"]/iframe')
        driver.switch_to_frame(iframe)
        selectBox = driver.find_element(By. XPATH, '//*[@id="speed-button"]/span[2]')
        selectBox.click()
        time.sleep(2)
        
ff = login()
ff.test()
