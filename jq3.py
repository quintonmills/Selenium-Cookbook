from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
class login():
    #sortable Recipe
    def test(self):
        baseUrl = "https://www.jQueryui.com"
        driver = webdriver.Chrome(executable_path="/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        sortableLink = driver.find_element(By. XPATH, '//*[@id="sidebar"]/aside[1]/ul/li[5]/a')
        sortableLink.click()
        time.sleep(2)
        iframe = driver.find_element(By. XPATH, '//*[@id="content"]/iframe')
        driver.switch_to_frame(iframe)
        itemOne = driver.find_element(By. XPATH, '//*[@id="sortable"]/li[1]')
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(itemOne, 0, 100).perform()
            print("drag on list successful")
            time.sleep(3)
        except:
                print("drag was unsuccessful")
ff = login()
ff.test()
