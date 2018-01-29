""" facebook login """

from time import sleep
from selenium import webdriver

USER = ''     #add your user name
PASS = ''     #add your password

DRIVER = webdriver.Chrome()
DRIVER.get('https://www.facebook.com/')
print("Opened facebook")

USERNAME = DRIVER.find_element_by_id('email')
USERNAME.send_keys(USER)
print("Email Id entered")

PASSWORD = DRIVER.find_element_by_id('pass')
PASSWORD.send_keys(PASS)
print("Password entered")

LOGIN_BTN = DRIVER.find_element_by_id('loginbutton')
LOGIN_BTN.click()

input('Press anything to quit')
DRIVER.quit()
print("Finished")
