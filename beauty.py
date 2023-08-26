from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os
from datetime import date
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Returns the current local date
current_time = datetime.datetime.now()
x = datetime.datetime(2024, 7, 1)
time = str(x.month) + "-" + str(x.year)
month_time = str(x.month)
print(month_time)
print(str(x.month) + "-" + str(x.year))

path = "C:/Users/tg1007599/OneDrive - DENSO/Khessarin/Energy/" + time

if month_time == "1":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "2":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "3":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "4":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "5":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "6":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "7":
    try:
        os.mkdir(path)
        print("Folder %s/Denso.xlsx created!" % path)
    except FileExistsError:
        print("Folder %s/Denso.xlsx already exists" % path)
elif month_time == "8":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "9":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "10":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "11":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
elif month_time == "12":
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)

# try:
#     os.mkdir(path)
#     print("Folder %s created!" % path)
# except FileExistsError:
#     print("Folder %s already exists" % path)


# url = "http://172.23.36.47:5500/output.html"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")
# table = soup.find("table", {"id": "ContentPlaceHolder1_gv_Report_DXMainTable"})
# tbody = table.find("tbody")
# data = []
# for row in table.find_all("tr"):
#     row_data = []
#     for cell in row.find_all("td"):
#         row_data.append(cell.text)
#     data.append(row_data)
#     df = pd.DataFrame(data)
# print(df)
# df.to_excel(
#     r"Denso1_1.xlsx",
#     sheet_name="BPK Feeder 1",
#     header=[
#         "Date",
#         "Max kW Peak",
#         "Max kW Off Peak",
#         "Max kW Holiday",
#         "kWh Peak",
#         "kWh Off Peak",
#         "kWh Holiday",
#         "Total kWh",
#         "Avg PF",
#         "",
#     ],
# )
# print(df)
