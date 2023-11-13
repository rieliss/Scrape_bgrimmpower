from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service

from bs4 import BeautifulSoup
import requests
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
    edgeService = Service(r"msedgedriver.exe")
    browser = webdriver.Edge(service=edgeService)
    # Simply just open a new Edge browser and go to lambdatest.com
    browser.maximize_window()
    browser.get("https://measmartlife.mea.or.th/measl/SLPlus/")
    try:
        myElem_1 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "uniqName_20_0"))
        )
        myElem_1.send_keys("slp55022555mlp")
        myElem_1.click()
        myElem_2 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "uniqName_20_1"))
        )
        myElem_2.send_keys("Co2Neutral")
        myElem_2.click()
        myElem_3 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), 'เข้าสู่ระบบ')]")
                )
            )
            .click()
        )
        sleep(5)
        myElem_4 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), 'ยอมรับ')]")
                )
            )
            .click()
        )
        sleep(5)
        myElem_5 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), 'Load Profile')]")
                )
            )
            .click()
        )
        myElem_6 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='label' and text()='รายเดือน']")
                )
            )
            .click()
        )
        myElem_7 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.XPATH, "//div[@id='amos_uniqName_24_3']/div[@class='amos-textbox-container']/div[@class='amos-textbox-input']/div[@class='amos-textbox-layout']/div[@class='amos-textbox-layout-item']/div[@class='amos-textbox-layout']")))
            .click()
        )
        myElem_8 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='amos-dropdown-inner']/ul[@class='amos-list-ul-item']/li[@data-amos-prop-displayed-value='" + month + "']")
                )
            )
            .click()
        )
        myElem_7 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), 'ค้นหา')]")
                )
            )
            .click()
        )
        sleep(10)
        myElem_10 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), 'kWh')]")
                )
            )
            .click()
        )
        sleep(10)
        soup = BeautifulSoup(browser.page_source, "lxml")
        Co2Neutral = []
        table = soup.find(
            "table", {"data-dojo-attach-point": "_tblNode"}
        )
        table_body = table.find("tbody" , attrs={"class": "zone-data"})
        for row in table.find_all("tr"):
            row_data = []
            for cell in row.find_all("td"):
                row_data.append(cell.text)
            Co2Neutral.append(row_data)
            Co2 = pd.DataFrame(Co2Neutral)
            dflist = Co2.dropna()
        print(dflist)
        dflist.pop(dflist.columns[0])
        print(dflist)
        dflist.to_excel(
            path + "/SRG_slp55022555mlp.xlsx",
            sheet_name="SRG_slp55022555mlp",
            header=[
                "Date",
                "khW(On-Peak)",
                "khW(Off-Peak)",
            ],
        )
        print("Write SRG Co2 Successfully!")
        sleep(3)
        print("Completed!")
        browser.close()
    except Exception as error:
        print("An exception occurred:", type(error).__name__)
    browser.close()
