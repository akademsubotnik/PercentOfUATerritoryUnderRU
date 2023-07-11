import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup():
    os.environ['PATH'] += r"C:\Users\Chuwi\PycharmProjects\UaRu\chromedriver_win32\chromedriver"
    driver = webdriver.Chrome()
    driver.get("https://deepstatemap.live/")
    return driver

def popups(driver):
    # popups
    try:
        driver.implicitly_wait(3)  # wait until element loads (timeout 3 seconds)
        ad1 = driver.find_element("xpath", "/html/body/div[12]/div/div[1]")
        ad1.click()
        driver.implicitly_wait(3)  # wait until element loads (timeout 3 seconds)
        rules = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/button[2]")
        rules.click()
        driver.implicitly_wait(3)  # wait until element loads (timeout 3 seconds)
    except:
        print('No element found.  Skipping')
    return driver
