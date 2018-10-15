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
        datePicker = driver.find_element(By. XPATH, "//a[contains(text(),'Checkboxradio')]")
        datePicker.click()
        time.sleep(3)
        frame = driver.find_element(By. XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to_frame(frame)
        button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/fieldset[1]/label[2]")
        button.click()
        time.sleep(2)
ff=login()
ff.test()
#<label for="radio-2" class="ui-checkboxradio-label ui-corner-all ui-button ui-widget ui-checkboxradio-radio-label"><span class="ui-checkboxradio-icon ui-corner-all ui-icon ui-icon-background ui-icon-blank"></span><span class="ui-checkboxradio-icon-space"> </span>Paris</label>