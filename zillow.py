from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login():

    def test(self):
        baseUrl = "https://www.zillow.com"
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        search = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]")
        search.click()
        search.send_keys("Atlanta")
        button = driver.find_element_by_xpath("//span[@class='search-button-text']")
        button.click()
        driver.implicitly_wait(10)
        #button = driver.find_element_by_xpath("//input[@value='Go']")
        #button.click()
ff = login()
ff.test()