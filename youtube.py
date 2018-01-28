"""youtube downloader"""

from time import sleep
from selenium import webdriver

MAIN_URL = 'https://www.youtube.com/'

KEYWORD = input('Enter keywords to search:  ')

SUB_URL = MAIN_URL + "results?search_query=" + KEYWORD.replace(" ", "+")

DRIVER = webdriver.Chrome()
DRIVER.get(SUB_URL)
print("Opened results page")
sleep(1)

SEARCH_BOX = DRIVER.find_element_by_id('search')
SEARCH_BOX.send_keys(KEYWORD)
print("keyword entered")
sleep(1)

SEARCH_BOX = DRIVER.find_element_by_id('search-icon-legacy')
SEARCH_BOX.click()
sleep(20)

ITEMS_ON_PAGE = DRIVER.find_element_by_id('video-title').get_attribute('title')
print(ITEMS_ON_PAGE)

print("Done")

input('Press anything to quit bitch')
DRIVER.quit()

print("Finished")
