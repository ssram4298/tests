""" facebook login and logout  """

from time import sleep
from selenium import webdriver

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

# logout1 = DRIVER.find_element_by_css_selector("#pageLoginAnchor")
# logout1.click()
# sleep(20)
# logout2 = DRIVER.find_element_by_css_selector("").submit()
print("Done")

input('Press anything to quit bitch')
DRIVER.quit()
print("Finished")
