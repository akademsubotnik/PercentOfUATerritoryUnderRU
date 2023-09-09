"""module to show percent of UA land occupied by RU"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Fnxn:
    """class to show percent of UA land occupied by RU"""    
    def setup(self):
        """function to create webdriver"""
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        service = Service(executable_path=r'chromedriver-linux64/chromedriver')
        driver = webdriver.Chrome(service=service, options=options)
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
        except Exception:
            print('No element found.  Skipping')
        return driver

    def donetsk_ot(self, driver) -> str:
        """"Get OT for Donetsk Region"""
        #Gets occupied territory Donetsk 1
        ot1=driver.find_element("xpath","/html/body/div[9]/div[1]/div[4]/img[151]")#Donetsk city
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(ot1, 20, 0)
        action.click()
        action.perform()
        ot1_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
        donetsk_ot = ot1_size.text
        print(f"Donetsk OT: {donetsk_ot}")
        time.sleep(1)
        #close it!
        close_1=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
        action.move_to_element_with_offset(close_1, 0, 0)
        action.click()
        action.perform()
        time.sleep(1)
        return donetsk_ot

    def lugansk_ot(self, driver) -> str:
        """"Get OT for Lugansk Region"""
        #Gets occupied territory Lugansk 1
        ot2=driver.find_element("xpath","/html/body/div[9]/div[1]/div[4]/img[82]")#(staroblisk lugansk)
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(ot2, 0, 20)
        action.click()
        action.perform()
        ot2_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
        lugansk_ot = ot2_size.text
        print(f"Lugansk OT: {lugansk_ot}")
        time.sleep(1)
        #close it!
        close_2=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
        action.move_to_element_with_offset(close_2, 0, 0)
        action.click()
        action.perform()
        time.sleep(1)
        return lugansk_ot

    def zaporozye_ot(self, driver) -> str:
        """"Get OT for Zaporozye Region"""
        #Gets occupied territory Zaporozye 1
        ot3=driver.find_element("xpath","/html/body/div[9]/div[1]/div[4]/img[165]")#melitopol(Zaporozye)
        #/html/body/div[9]/div[1]/div[4]/img[169]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(ot3, 20, 0)
        action.click()
        action.perform()
        ot3_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
        zaporozye_ot = ot3_size.text
        print(f"Zaporozye OT: {zaporozye_ot}")
        time.sleep(1)
        #close it!
        close_3=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
        action.move_to_element_with_offset(close_3, 0, 0)
        action.click()
        action.perform()
        time.sleep(1)
        return zaporozye_ot
