import os
from selenium import webdriver

#config
os.environ['PATH'] += r"C:\Users\Chuwi\PycharmProjects\UaRu\chromedriver_win32\chromedriver"
driver = webdriver.Chrome()
driver.get("https://deepstatemap.live/")

#popups
try:
    driver.implicitly_wait(3) #wait until element loads (timeout 3 seconds)
    ad1 = driver.find_element("xpath", "/html/body/div[12]/div/div[1]")
    ad1.click()
    driver.implicitly_wait(3) #wait until element loads (timeout 3 seconds)
    rules = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/button[2]")
    rules.click()
    driver.implicitly_wait(3) #wait until element loads (timeout 3 seconds)
except:
    print('No element found.  Skipping')


#map
zapor = driver.find_element("xpath", '//*[@id="map"]/div[1]/div[6]/div/div[1]/div/i')
#zapor.click()
print(zapor.text)
driver.implicitly_wait(3) #wait until element loads (timeout 3 seconds)


#ot1 = driver.find_element("xpath", '//*[@id="map"]/div[1]/div[6]/div/div[1]/div/i')
#print(ot1.text)
#driver.implicitly_wait(3) #wait until element loads (timeout 3 seconds)
