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

driver = f1.setup()
driver = f1.popups(driver)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#I would like to pass "style="opacity: 1; transform: translate3d(1201px, 442px, 0px); bottom: -7px; left: -74px;"" to the click.
#opacity: 1; transform: translate3d(1284px, 499px, 0px); bottom: -7px; left: -80px;

ot1 = driver.find_element("xpath", '/html/body/div[9]/div[1]/div[6]')
#driver.execute_script("arguments[0].setAttribute('style', 'opacity: 1; transform: translate3d(1284px, 499px, 0px); bottom: -7px; left: -80px;').click();", ot1)
#driver.execute_script("$('#emailItinerarySuccessModal .indigo-submit').click();", ot1)
js = driver.execute_script
js("arguments[0].setAttribute('style', 'opacity: 1; transform: translate3d(1284px, 499px, 0px); bottom: -7px; left: -80px;')", ot1)
print(ot1.children)

#driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")
#ot1.click()



# Execute JavaScript to set attribute style
# js = driver.execute_script
# element1 = driver.find_element(By.XPATH, "//div[contains(@class,'rmSlide')]")
# js("arguments[0].setAttribute('style', 'visibility: visible; height: 259px; width: 339px; display: block; overflow: hidden; left: -81px; top: 24px; z - index: 2; ')", element1)





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
