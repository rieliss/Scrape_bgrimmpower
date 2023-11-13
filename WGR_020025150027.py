from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait


from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import datetime

current_time = datetime.datetime.now()
# current_time = datetime.datetime(2023, 7, 1)
time = str(current_time.month) + "-" + str(current_time.year)
month_time = str(current_time.month)
print(month_time)
print(str(current_time.month) + "-" + str(current_time.year))

path = "//172.23.3.44/public/Energy/" + time
month = ""

if month_time == "1":
    month = 'มกราคม'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "2":
    month = 'กุมภาพันธ์'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "3":
    month = 'มีนาคม'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "4":
    month = 'เมษายน'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "5":
    month = 'พฤษภาคม'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "6":
    month = 'มิถุนายน'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "7":
    month = 'กรกฎาคม'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "8":
    month = 'สิงหาคม'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "9":
    month = 'กันยายน '
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "10":
    month = 'ตุลาคม'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "11":
    month = 'พฤศจิกายน'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "12":
    month = 'ธันวาคม'
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)

if __name__ == "__main__":
    browser = webdriver.Edge(r"msedgedriver.exe")
    browser.maximize_window()
    browser.get("https://www.amr.pea.co.th/AMRWEB/Index.aspx")
    wait = WebDriverWait(browser, 10)
    try:
        myElem_1 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "txtUserName"))
        )
        myElem_1.send_keys("020025150027")
        myElem_1.click()
        myElem_2 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "txtPassword"))
        )
        myElem_2.send_keys("denso1234")
        myElem_2.click()
        myElem_3 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.ID, "btnOK")
                )
            )
            .click()
        )
        sleep(3)
        myElem_4 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), 'โหลดโปรไฟล์')]")
                )
            )
            .click()
        )
        sleep(3)
        myElem_5 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@id='divMenu3']/div[@class='menusub']/span[contains(text(), 'รายเดือน')]")
                )
            )
            .click()
        )
        radio_button = browser.find_element(By.XPATH, "//div[@id='divMenu3']/div[@class='menusub']/span[contains(text(), 'รายเดือน')]")
        print(radio_button.text)
        soup = BeautifulSoup(browser.page_source, "lxml")
        print(soup)
        sleep(30)
        print("Completed!")
        browser.close()
    except Exception as error:
        print("An exception occurred:", type(error).__name__)
    sleep(50)
    browser.close()