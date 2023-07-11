import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from functions import setup, popups

driver = setup()
driver = popups(driver)

#map
ot1 = driver.find_element("xpath", '//*[@id="map"]')
ot1.click()
#print(zapor.text)
driver.implicitly_wait(3) #wait until element loads (timeout 3 seconds)
time.sleep(5) #sleep for 1 sec

#click an area on the map by coordiantes for each OT???
