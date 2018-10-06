
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login():

    def test(self):
        baseUrl = "https://www.amazon.com"
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)
        itemSearch = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/input[1]")
        itemSearch.send_keys("xbox console")
        searchItem = driver.find_element_by_xpath("//input[@value='Go']")
        searchItem.click()
        driver.implicitly_wait(3)
        itemSelect = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/h2[1]")
        itemSelect.click()
        addToCart = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[7]/div[4]/div[1]/div[1]/div[14]/div[1]/div[1]/form[1]/div[1]/div[10]/div[1]/span[1]/span[1]/input[1]")
        addToCart.click()
        insurance = driver.find_element_by_xpath("/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]")
        insurance.click()
ff = login()
ff.test()