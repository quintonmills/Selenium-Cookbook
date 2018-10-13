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
        menuSelection = driver.find_element(By. XPATH, "//a[contains(text(),'Selectmenu')]")
        menuSelection.click()
        driver.implicitly_wait(1)
        driver.switch_to.frame(0)
        speedButton = driver.find_element(By. XPATH, "/html[1]/body[1]/div[1]/form[1]/fieldset[1]/span[1]/span[2]")
        speedButton.click()
        time.sleep(2)
        speedSelect = driver.find_element(By. XPATH, '/html[1]/body[1]/div[2]/ul[1]/li[2]/div[1]')
        speedSelect.click()
        time.sleep(2)
ff = login()
ff.test()
