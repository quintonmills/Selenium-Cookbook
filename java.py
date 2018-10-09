from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(4)
        time.sleep(5)
        elementSelect = driver.execute_script("return document.getElementById('name');")
        elementSelect.send_keys("Yeah Boii")

ff = JavaScriptExecution()
ff.test()