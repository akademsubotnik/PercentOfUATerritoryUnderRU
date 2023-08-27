"""module to show percent of UA land occupied by RU"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class Fnxn:
    """class to show percent of UA land occupied by RU"""
    def setup(self):
        """function to create webdriver"""
        #chrome_options = Options()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        #os.environ['PATH'] += r"C:\Users\Chuwi\PycharmProjects\UaRu\chromedriver_win32\chromedriver"
        service = Service(executable_path=r'/workspaces/PercentOfUATerritoryUnderRU/chromedriver-linux64/chromedriver')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://deepstatemap.live/")
        html = driver.page_source
        time.sleep(2)
        print(html)
        driver.quit()
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
