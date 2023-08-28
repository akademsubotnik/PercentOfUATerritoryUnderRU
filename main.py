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

#to get number
import re

f1 = Fnxn()

driver = f1.setup_githubcodespaces()
driver = f1.popups(driver)


#Gets occupied territory Donetsk 1
ot1=driver.find_element("xpath","/html/body/div[9]/div[1]/div[4]/img[151]")#Donetsk city
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(ot1, 20, 0)
action.click()
action.perform()
ot1_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
print(ot1_size.text)
donetsk_ot = ot1_size.text
#close it!
close_1=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
action.move_to_element_with_offset(close_1, 0, 0)
action.click()
action.perform()

time.sleep(10)

#Gets occupied territory Lugansk 1
ot2=driver.find_element("xpath","/html/body/div[9]/div[1]/div[4]/img[84]")#starobilsk(Lugansk)
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(ot2, 0, 20)
action.click()
action.perform()
ot2_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
print(ot2_size.text)
lugansk_ot = ot2_size.text
#close it!
close_2=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
action.move_to_element_with_offset(close_2, 0, 0)
action.click()
action.perform()


#Gets occupied territory Zaporozye 1
ot3=driver.find_element("xpath","/html/body/div[9]/div[1]/div[4]/img[169]")#melitopol(Zaporozye)
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(ot3, 20, 0)
action.click()
action.perform()
ot3_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")

print(ot3_size.text)
zaporozye_ot = ot3_size.text
#print(type(str(zaporozye_ot)))
#close it!
close_3=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
action.move_to_element_with_offset(close_3, 0, 0)
action.click()
action.perform()


donot = donetsk_ot.split()
print(donot[1])

logot = lugansk_ot.split()
print(logot[1])

zapot = zaporozye_ot.split()
print(zapot[1])


total_occupied = float(donot[1]) + float(logot[1]) + float(zapot[1])
print(total_occupied)
total_size = 576700.00

percent_occupied = (total_occupied / total_size) * 100
print("Percent Occupied: " + str(percent_occupied) + "%")

time.sleep(10)

