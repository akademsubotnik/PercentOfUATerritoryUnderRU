"""module to show percent of UA land occupied by RU"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Fnxn:
    """class to show percent of UA land occupied by RU"""
    def setup(self):
        """function to create webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--auto-open-devtools-for-tabs")
        os.environ['PATH'] += r"C:\Users\Chuwi\PycharmProjects\UaRu\chromedriver_win32\chromedriver"
        driver = webdriver.Chrome(chrome_options)
        driver.get("https://deepstatemap.live/")
        return driver

    def popups(self, driver):
        """function to close popups"""
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
