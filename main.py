"""main.py"""
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

driver = f1.setup_localvscode()
driver = f1.popups(driver)


el=driver.find_element("xpath","/html/body/div[9]/div[1]/div[4]/img[119]")
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(el, 0, -20)
#action.move_by_offset(1200,400) #x left side to right side is ~2000 px , #y from bottom to top is ~1300
action.click()
action.perform()

ot1 = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
print(ot1.text)
time.sleep(50)


#    -x+y | +x+y
#    =============   
#    -x-y | +x-y
#         |
#https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
# move_by_offset(xoffset, yoffset)
# Moving the mouse to an offset from current mouse position.

# Args:	
# xoffset: X offset to move to, as a positive or negative integer.
# yoffset: Y offset to move to, as a positive or negative integer.
# move_to_element(to_element)
# Moving the mouse to the middle of an element.

# Args:	
# to_element: The WebElement to move to.
# move_to_element_with_offset(to_element, xoffset, yoffset)
# Move the mouse by an offset of the specified element. Offsets are relative to the in-view center point of the element.

# Args:	
# to_element: The WebElement to move to.
# xoffset: X offset to move to, as a positive or negative integer.
# yoffset: Y offset to move to, as a positive or negative integer.
