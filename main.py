import os
import time
from selenium import webdriver
# #from selenium.webdriver import Keys
# #from selenium.webdriver.common.by import By
# from class_functions import Fnxn


from chromedriver_py import binary_path # this will get you the path variable

svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)

# deprecated but works in older selenium versions
# driver = webdriver.Chrome(executable_path=binary_path)
driver.get("http://www.python.org")
assert "Python" in driver.title

# f1 = Fnxn()


# driver = f1.setup()
# driver = f1.popups(driver)

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
