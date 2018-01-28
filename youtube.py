""" Youtube Downloader """

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SEARCH = input("enter your search: ")

try:
    R = requests.get("https://www.youtube.com/results?search_query=" + SEARCH)

    SOUP = BeautifulSoup(R.content, "html.parser")

    RESULTS = SOUP.find_all("h3", {"class": "yt-lockup-title"})

    COUNT = 1
    VIDEOS = []
    MY_LIST = []

    for items in RESULTS:
        MY_LIST.append(items.a.text)
        VIDEOS.append(items.a["href"])

    print("List Of Videos Found")
    print("=================================")
    for i in MY_LIST:
        print(str(COUNT) + ')' + i)
        COUNT += 1

    print("================================")
    CHOICE = int(input("Enter Your Choice: "))

    OUTPUT = "https://youtube.com" + VIDEOS[CHOICE-1]

    DRIVER = webdriver.Chrome()
    DRIVER.get("http://en.savefrom.net/")

    try:
        SUBMIT = WebDriverWait(DRIVER, 10).until(
            EC.presence_of_element_located((By.ID, "sf_submit"))
        )
        LINK_BOX = WebDriverWait(DRIVER, 10).until(
            EC.presence_of_element_located((By.ID, "sf_url"))
        )
        LINK_BOX.send_keys(OUTPUT)
        print("entered address")
        SUBMIT.click()
        print("submit button clicked")

        try:
            DROP_BOX = WebDriverWait(DRIVER, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "drop-down-box"))
            )

            SOUP = BeautifulSoup(DRIVER.page_source, "html.parser")
            QUALITY = SOUP.find("div", {"class":"drop-down-box"})
            ITEMS = QUALITY.find_all("a")
            QUALITY_LIST = []
            VIDEO_LINKS = []
            for it in ITEMS:
                QUALITY_LIST.append(it.text)
                VIDEO_LINKS.append(it["href"])

            COUNT2 = 1
            for i in QUALITY_LIST:
                print(str(COUNT2) +")"+i)
                COUNT2 += 1

            print("===============================")
            CHOICE = int(input("Enter your choice: "))
            print("===============================")
            print("Your video is being downloaded...............")
            DRIVER.get(VIDEO_LINKS[CHOICE - 1])

        finally:
            print("done!")
    finally:
        print("submit button clicked")

except R:
    print("**************************************")
    print("Can't connect to youtube")
    print("**************************************")
