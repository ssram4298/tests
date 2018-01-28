""" Youtube Downloader """

# from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


search = input("enter your search: ")
r = requests.get("https://www.youtube.com/results?search_query=" + search)

soup = BeautifulSoup(r.content, "html.parser")

results = soup.find_all("h3", {"class": "yt-lockup-title"})

COUNT = 1
VIDEOS = []
MY_LIST = []

for items in results:
    MY_LIST.append(items.a.text)
    VIDEOS.append(items.a["href"])

print("List Of Videos Found")
print("=================================")
for i in MY_LIST:
    print(str(COUNT) + ')' + i)
    COUNT += 1

print("================================")
choice = int(input("Enter Your Choice: "))

output = "https://youtube.com" + VIDEOS[choice-1]

driver = webdriver.Chrome()
driver.get("http://en.savefrom.net/")

try:
    submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sf_submit"))
    )
    link_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sf_url"))
    )
    link_box.send_keys(output)
    print("entered address")
    submit.click()
    print("submit button clicked")

    try:
        drop_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "drop-down-box"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")
        quality = soup.find("div", {"class":"drop-down-box"})
        itms = quality.find_all("a")
        lst = []
        vid = []
        for it in itms:
            lst.append(it.text)
            vid.append(it["href"])

        ct = 1
        for i in lst:
            print(str(ct)+")"+i)
            ct += 1

        print("===============================")
        choice = int(input("Enter your choice: "))
        print("===============================")
        print("Your video is being downloaded...............")
        driver.get(vid[choice-1])

    finally:
        print("done!")
finally:
    print("submit button clicked")
