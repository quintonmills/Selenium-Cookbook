from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
class login():

    def test(self):
        baseUrl = "http://jqueryui.com/"
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        datePicker = driver.find_element(By. XPATH, "//a[contains(text(),'Datepicker')]")
        datePicker.click()
        time.sleep(3)
        frame = driver.find_element(By. XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to_frame(frame)
        date = driver.find_element_by_class_name("hasDatepicker")
        #dateField = driver.find_element(By. class,'hasDatepicker')
        date.click()
        datePick = driver.find_element_by_partial_link_text("16")
        datePick.click()
        time.sleep(2)
ff=login()
ff.test()