from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
class login():
    #resizable Recipe
    def test(self):
        baseUrl = "https://www.jQueryui.com"
        driver = webdriver.Chrome(executable_path="/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        resizableLink = driver.find_element(By. XPATH, "//a[contains(text(),'Resizable')]")
        resizableLink.click()
        frame = driver.find_element(By. XPATH, "//*[@id='content']/iframe")
        driver.switch_to_frame(frame)
        resizableElement = driver.find_element(By. XPATH, "//*[@id='resizable']/div[3]")
        #<div class="ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se" 
        try:
            actions = ActionChains(driver)
            actions.click_and_hold(resizableElement).move_by_offset(50,50).release().perform()
            print("drag successful")
        except:
            print("drag unsuccessful")
        time.sleep(2)
ff=login()
ff.test()


