"""module to show percent of UA land occupied by RU"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from typing import Final

site_name: Final = "https://deepstatemap.live/"
#sn: Final = "https://wikipedia.com/wiki/Main_Page"

class Fnxn:
    """class to show percent of UA land occupied by RU"""    
    def setup(self):
        """function to create webdriver"""
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--auto-open-devtools-for-tabs')
        #options.add_argument('--kiosk')
        service = Service(executable_path=r'chromedriver-linux64/chromedriver')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://deepstatemap.live/')
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
            
        driver.maximize_window()
        return driver

    def donetsk_ot(self, driver) -> str:
        """"Get OT for Donetsk Region"""
        
        #Move by offset
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_by_offset(1114, 600)
        action.click()
        action.perform()
        
        #Get size, should be standard
        ot1_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
        donetsk_ot = ot1_size.text
        print(f"Donetsk OT: {donetsk_ot}")
        time.sleep(1)
        
        #Close it, should be standard
        #close it!
        close_1=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
        action.move_to_element_with_offset(close_1, 0, 0)
        action.click()
        action.perform()
        time.sleep(1)
        
        
        # #Reset offset
        # action = webdriver.common.action_chains.ActionChains(driver)
        # action.move_by_offset(-1114, -600)
        # action.perform()
        
        return donetsk_ot

    def lugansk_ot(self, driver) -> str:
        """"Get OT for Lugansk Region"""
        
        #Move by offset
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_by_offset(-107,-297)      #1007,303
        action.click()
        action.perform()
        time.sleep(5)
        
        #Get size, should be standard
        ot2_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
        lugansk_ot = ot2_size.text
        print(f"Lugansk OT: {lugansk_ot}")
        time.sleep(1)
        
        #Close it, should be standard
        #close it!
        close_2=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
        action.move_to_element_with_offset(close_2, 0, 0)
        action.click()
        action.perform()
        time.sleep(1)
        return lugansk_ot

    def zaporozye_ot(self, driver) -> str:
        """"Get OT for Zaporozye Region"""
        
        #Move by offset
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_by_offset(970, 771)
        action.click()
        action.perform()
        time.sleep(5)

        #Get size, should be standard
        ot3_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
        zaporozye_ot = ot3_size.text
        print(f"Zaporozye OT: {zaporozye_ot}")
        time.sleep(1)
        
        #Close it, should be standard
        #close it!
        close_3=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
        action.move_to_element_with_offset(close_3, 0, 0)
        action.click()
        action.perform()
        time.sleep(1)
        return zaporozye_ot