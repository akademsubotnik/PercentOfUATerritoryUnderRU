"""main.py"""
import time
from typing import Final
from datetime import date


#Selenium Imports
#from selenium import webdriver

#Class imports
from class_functions import Fnxn

TOTAL_SIZE: Final = 576700.00


f1 = Fnxn()

driver = f1.setup()
time.sleep(5)
driver.maximize_window()
#driver = f1.popups(driver)
time.sleep(5)

#TO GET ELEMENT LOCATION, RUN  https://stackoverflow.com/questions/26820942/browser-developer-tools-what-is-the-position-of-the-html-element
# $0.getBoundingClientRect() with element focused and use x and y as values for get by offset function!!!

zaporozye_ot = f1.mbo(driver)
time.sleep(10)