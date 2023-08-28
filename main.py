"""main.py"""
import time
from typing import Final

#Selenium Imports
#from selenium import webdriver

#Class imports
from class_functions import Fnxn

TOTAL_SIZE: Final = 576700.00


f1 = Fnxn()

driver = f1.setup()
driver = f1.popups(driver)
time.sleep(10)

#Get value of occupied regions
donetsk_ot = f1.donetsk_ot(driver)
time.sleep(10)
lugansk_ot = f1.lugansk_ot(driver)
time.sleep(10)
zaporozye_ot = f1.zaporozye_ot(driver)
time.sleep(10)

#Get float value of occupied regions
donot = donetsk_ot.split()
print(donot[1])
logot = lugansk_ot.split()
print(logot[1])
zapot = zaporozye_ot.split()
print(zapot[1])


#Do some math
total_occupied = float(donot[1]) + float(logot[1]) + float(zapot[1])
print(total_occupied)

percent_occupied = (total_occupied / TOTAL_SIZE) * 100
print("Percent Occupied: " + str(percent_occupied) + "%")

time.sleep(10)
