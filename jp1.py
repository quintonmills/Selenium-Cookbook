from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
class login():
    def test(self):
        baseUrl = "https://www.jQueryui.com"
        driver = webdriver.Chrome(executable_path ="/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(2)
        draggableLink = driver.find_element(By. XPATH, "//div[@id='sidebar']//aside[1]//ul[1]//li[1]")
        draggableLink.click()
        time.sleep(2)
        iframe = driver.find_element(By. XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to_frame(iframe)
        draggableElement = driver.find_element(By. XPATH, '//body/div[1]')
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(draggableElement,100,100).perform()
            print("drag and drop successful")
        except:
            print("drag unsuccessful")
        time.sleep(2)
        
ff = login()
ff.test()