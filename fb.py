""" facebook login and logout  """

from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

USER = '8019886716'
PASS = 'srasta4007@'

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

sleep(10)
LOGOUT1 = DRIVER.find_element_by_css_selector("#userNavigationLabel")
LOGOUT1.click()
sleep(10)

# try:
#     LOGOUT1 = WebDriverWait(DRIVER, 10).until(
#         EC.presence_of_element_located((By.ID, "userNavigationLabel")),
#         EC.element_to_be_clickable((By.ID, "userNavigationLabel"))
#     )
#     print("button found")
#     LOGOUT1.click()
#     try:
#         LOGOUT2 = WebDriverWait(DRIVER, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR,
#               "._w0d[action='https://www.facebook.com/logout.php']"))
#         )
#         LOGOUT2.submit()
#     finally:
#         print("logout button found")
# finally:
#     print("element clicked")

input('Press anything to quit bitch')
DRIVER.quit()
print("Finished")
