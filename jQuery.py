from selenium import webdriver
from selenium.webdriver.common.by import By
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
        menuSelection = driver.find_element(By. XPATH, "//a[contains(text(),'Droppable')]")
        menuSelection.click()
        time.sleep(3)
        driver.switch_to.frame(0)
        fromElement = driver.find_element(By.XPATH, '//body/div[1]')
        toElement = driver.find_element(By. XPATH, '//body/div[2]')
        time.sleep(3)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(fromElement, toElement).perform()
            print("drag and drop successful")
        except:
            print("drag unsuccessful")
        
ff=login()
ff.test()
        
