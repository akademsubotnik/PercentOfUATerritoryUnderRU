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

driver = f1.setup_localvscode()
driver = f1.popups(driver)


#Gets occupied territory Donetsk 1
ot1=driver.find_element("xpath","/html/body/div[9]/div[1]/div[4]/img[151]")#Donetsk city
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(ot1, 20, 0)
action.click()
action.perform()
ot1_size = driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/div[1]/div/i")
print(ot1_size.text)
donetsk_ot = ot1_size
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
lugansk_ot = ot2_size
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
zaporozye_ot = ot3_size
#close it!
close_3=driver.find_element("xpath","/html/body/div[9]/div[1]/div[6]/div/a")
action.move_to_element_with_offset(close_3, 0, 0)
action.click()
action.perform()

print(str(donetsk_ot) + str(lugansk_ot) + str(zaporozye_ot))
#[int(s) for s in txt.split() if s.isdigit()]

#lugansk_ot = re.findall(r'\d+', str(ot1_size))
#donetsk_ot = re.findall(r'\d+', str(ot2_size))
#zaporozye_ot = re.findall(r'\d+', str(ot3_size))

#total_occupied = lugansk_ot + donetsk_ot + zaporozye_ot
#print(total_occupied)
#total_size = 576700

percent_occupied = "a"

time.sleep(50)

