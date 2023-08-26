from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os
import datetime

current_time = datetime.datetime.now()
x = datetime.datetime(2024, 7, 1)
time = str(current_time.month) + "-" + str(current_time.year)
month_time = str(current_time.month)
print(month_time)
print(str(current_time.month) + "-" + str(current_time.year))

path = "//172.23.3.44/public/Energy/" + time

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
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
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


if __name__ == "__main__":
    browser = webdriver.Edge(r"msedgedriver.exe")
    browser.maximize_window()
    browser.get("https://smartview.bgrimmpower.com/Login")

    try:
        l1_denso1_1 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "txt_Username"))
        )
        l1_denso1_1.send_keys("DENSO1.1")
        l1_denso1_1.click()
        Click1_denso1_1 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "btn_Next")))
            .click()
        )
        l2_denso1_1 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "txt_Password"))
        )
        l2_denso1_1.send_keys("F#cilityBPK1.1")
        l2_denso1_1.click()
        c2_denso1_1 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "btn_Login")))
            .click()
        )
        c3_denso1_1 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), ' Daily TOU/TOD')]")
                )
            )
            .click()
        )
        c4_denso1_1 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_btn_View")))
            .click()
        )
        sleep(10)
        soup = BeautifulSoup(browser.page_source, "lxml")
        print(soup.prettify())
        # with open("output.html", "w", encoding="utf-8") as file:
        #     # prettify the soup object and convert it into a string
        #     file.write(str(soup.prettify()))
        data_denso1_1 = []
        table = soup.find(
            "table", attrs={"id": "ContentPlaceHolder1_gv_Report_DXMainTable"}
        )
        table_body = table.find("tbody")

        for row in table.find_all("tr"):
            row_data = []
            for cell in row.find_all("td"):
                row_data.append(cell.text)
            data_denso1_1.append(row_data)
            df_denso1_1 = pd.DataFrame(data_denso1_1)
            # print(data_denso1_1)
            # df_denso1_1 = pd.DataFrame(data_denso1_1)
            df_denso1_1 = df_denso1_1[1:]
        # print(df_denso1_1)
        df_denso1_1.to_excel(
            path + "/Denso1_1.xlsx",
            sheet_name="BPK Feeder 1",
            header=[
                "Date",
                "Max kW Peak",
                "Max kW Off Peak",
                "Max kW Holiday",
                "kWh Peak",
                "kWh Off Peak",
                "kWh Holiday",
                "Total kWh",
                "Avg PF",
                "",
            ],
        )
        print(df_denso1_1)
        print("Write DENSO 1.1 Successfully!")
        sleep(10)
        c5_denso1_1 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "navbarDropdown")))
            .click()
        )
        c6_denso1_1 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), ' Log Out')]")
                )
            )
            .click()
        )

        l1_denso1_2 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "txt_Username"))
        )
        l1_denso1_2.send_keys("DENSO1.2")
        l1_denso1_2.click()
        Click1_denso1_2 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "btn_Next")))
            .click()
        )
        l2_denso1_2 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "txt_Password"))
        )
        l2_denso1_2.send_keys("F#cilityBPK1.2")
        l2_denso1_2.click()
        c2_denso1_2 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "btn_Login")))
            .click()
        )
        c3_denso1_2 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), ' Daily TOU/TOD')]")
                )
            )
            .click()
        )
        c4_denso1_2 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_btn_View")))
            .click()
        )
        sleep(10)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_denso1_2 = []
        table = soup.find(
            "table", attrs={"id": "ContentPlaceHolder1_gv_Report_DXMainTable"}
        )
        table_body = table.find("tbody")

        for row in table.find_all("tr"):
            row_data = []
            for cell in row.find_all("td"):
                row_data.append(cell.text)
            data_denso1_2.append(row_data)
            df_denso1_2 = pd.DataFrame(data_denso1_2)
            # print(data_denso1_2)
            # df_denso1_2 = pd.DataFrame(data_denso1_2)
            df_denso1_2 = df_denso1_2[1:]
        # print(df_denso1_2)
        df_denso1_2.to_excel(
            path + "/Denso1_2.xlsx",
            sheet_name="BPK Feeder 2",
            header=[
                "Date",
                "Max kW Peak",
                "Max kW Off Peak",
                "Max kW Holiday",
                "kWh Peak",
                "kWh Off Peak",
                "kWh Holiday",
                "Total kWh",
                "Avg PF",
                "",
            ],
        )
        print(df_denso1_2)
        print("Write DENSO 1.2 Successfully!")
        sleep(10)
        c5_denso1_2 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "navbarDropdown")))
            .click()
        )
        c6_denso1_2 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), ' Log Out')]")
                )
            )
            .click()
        )

        l1_denso1_3 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "txt_Username"))
        )
        l1_denso1_3.send_keys("DENSO1.3")
        l1_denso1_3.click()
        Click1_denso1_3 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "btn_Next")))
            .click()
        )
        l2_denso1_3 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "txt_Password"))
        )
        l2_denso1_3.send_keys("F#cilityBPK1.3")
        l2_denso1_3.click()
        c2_denso1_3 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "btn_Login")))
            .click()
        )
        c3_denso1_3 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), ' Daily TOU/TOD')]")
                )
            )
            .click()
        )
        c4_denso1_3 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_btn_View")))
            .click()
        )
        sleep(10)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_denso1_3 = []
        table = soup.find(
            "table", attrs={"id": "ContentPlaceHolder1_gv_Report_DXMainTable"}
        )
        table_body = table.find("tbody")

        for row in table.find_all("tr"):
            row_data = []
            for cell in row.find_all("td"):
                row_data.append(cell.text)
            data_denso1_3.append(row_data)
            df_denso1_3 = pd.DataFrame(data_denso1_3)
            # print(data_denso1_3)
            # df_denso1_3 = pd.DataFrame(data_denso1_3)
            df_denso1_3 = df_denso1_3[1:]
        # print(df_denso1_3)
        df_denso1_3.to_excel(
            path + "/Denso1_3.xlsx",
            sheet_name="BPK Feeder 3",
            header=[
                "Date",
                "Max kW Peak",
                "Max kW Off Peak",
                "Max kW Holiday",
                "kWh Peak",
                "kWh Off Peak",
                "kWh Holiday",
                "Total kWh",
                "Avg PF",
                "",
            ],
        )
        print(df_denso1_3)
        print("Write DENSO 1.3 Successfully!")
        sleep(10)
        c5_denso1_3 = (
            WebDriverWait(browser, 10)
            .until(EC.element_to_be_clickable((By.ID, "navbarDropdown")))
            .click()
        )
        c6_denso1_3 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), ' Log Out')]")
                )
            )
            .click()
        )
        print("Completed!")
        # browser.close()
    except TimeoutException:
        print("No element found")
    sleep(10)
    browser.close()
