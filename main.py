import os
import time

#Selenium Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# #from selenium.webdriver import Keys
# #from selenium.webdriver.common.by import By

#Class imports
from class_functions import Fnxn

f1 = Fnxn()

driver = f1.setup()
driver = f1.popups(driver)



# #map
# ot1 = driver.find_element("xpath", '//*[@id="map"]')
# ot1.click()
# #print(zapor.text)
# driver.implicitly_wait(3) #wait until element loads (timeout 3 seconds)
# time.sleep(100) #sleep for 1 sec

# #driver.find_element(By.CLASS_NAME, "leaflet-zoom-animated".style.opacity = '0';)
# #driver.execute_script("document.getElementByClassName('leaflet-zoom-animated').style.opacity = '0';")
# driver.find_element(By.XPATH, "/html/body").send_keys(Keys.TAB)
# driver.find_element(By.XPATH, "/html/body").send_keys(Keys.TAB)
# driver.find_element(By.XPATH, "/html/body").send_keys(Keys.F12)
# driver.find_element(By.XPATH, "/html/body").send_keys(Keys.TAB)
# driver.find_element(By.XPATH, "/html/body").send_keys(Keys.TAB)
# driver.find_element(By.XPATH, "/html/body").send_keys(Keys.TAB)
# driver.find_element(By.XPATH, "/html/body").send_keys(Keys.TAB)
# driver.find_element(By.XPATH, "/html/body").send_keys(Keys.ENTER)
# time.sleep(5)



#click an area on the map by coordiantes for each OT???
