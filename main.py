import os
from selenium import webdriver
import time

#config
os.environ['PATH'] += r"C:\Users\Chuwi\PycharmProjects\UaRu\chromedriver_win32\chromedriver"
driver = webdriver.Chrome()
driver.get("https://deepstatemap.live/")

#popups
time.sleep(5) #sleep for 1 sec
my_element = driver.find_element("xpath", "/html/body/div[12]/div/div[1]")
my_element.click()
time.sleep(5) #sleep for 1 sec
my_element2 = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/button[2]")
my_element2.click()
time.sleep(5) #sleep for 1 sec

