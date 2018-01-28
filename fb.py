""" facebook login and logout  """

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER = '8019886716'
PASS = 'srasta4007@'

DRIVER = webdriver.Chrome()
DRIVER.get('https://www.facebook.com/')
print("Opened facebook")
sleep(1)

USERNAME = DRIVER.find_element_by_id('email')
USERNAME.send_keys(USER)
print("Email Id entered")
sleep(1)

PASSWORD = DRIVER.find_element_by_id('pass')
PASSWORD.send_keys(PASS)
print("Password entered")

LOGIN_BTN = DRIVER.find_element_by_id('loginbutton')
LOGIN_BTN.click()

try:
    ELEMENT = WebDriverWait(DRIVER, 10).until(
        EC.presence_of_element_located(By.ID, "userNavigationLabel")
    )
finally:  
    print("element found")    

# LOGOUT1 = DRIVER.find_element_by_id("pageLoginAnchor")
# LOGOUT1.click()
# LOGOUT2 = DRIVER.find_element_by_xpath('//*[@id="u_1c_3"]').submit()

print("Done")

input('Press anything to quit bitch')
DRIVER.quit()
print("Finished")
