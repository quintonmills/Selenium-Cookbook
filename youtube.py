from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class search1():

    def test(self):
        baseUrl = "https://www.youtube.com"
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        Search = driver.find_element_by_xpath("//input[@id='search']")
        Search.click()
        Search.send_keys("Drake")
        icon = driver.find_element_by_xpath("//button[@id='search-icon-legacy']")
        icon.click()
        driver.implicitly_wait(3)
        video = driver.find_element_by_xpath("//div[@id='contents']//ytd-video-renderer[1]//div[1]//div[1]//div[1]//div[1]//h3[1]//a[1]")
        video.click()
        driver.implicitly_wait(3)
ff = search1()
ff.test()