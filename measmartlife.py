from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os
import datetime

# # load the projectpro webpage content
# r = requests.get("https://measmartlife.mea.or.th/measl/SLPlus/")

# # convert to beautiful soup
# soup = BeautifulSoup(r.content)

# # printing our web page
# print(soup.prettify())

# table = soup.select("table#dataTablesFaculties")[0]
# columns = table.find("thead").find_all("th")
# print(columns)

# table_df = pd.read_html(str(table))[0]
# print(table_df)

if __name__ == "__main__":
    # Instantiate the webdriver with the executable location of MS Edge
    edgeService = Service(r"D:\\Lambdatest Tools\\edgedriver_win64\\msedgedriver.exe")
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
        myElem_4 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), 'ยอมรับ')]")
                )
            )
            .click()
        )
        # sleep(10)
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
            .until(EC.element_to_be_clickable((By.CLASS_NAME, "div.item. selected")))
            .click()
        )
        print("myElem_6")
        # myElem_6 = (
        #     WebDriverWait(browser, 10)
        #     .until(
        #         EC.element_to_be_clickable(
        #             (By.XPATH, "//*[contains(text(), 'รายเดือน')]")
        #         )
        #     )
        #     .click()
        # )
        # myElem_7 = (
        #     WebDriverWait(browser, 10)
        #     .until(
        #         EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'ค้นหา')]"))
        #     )
        #     .click()
        # )
        # print("myElem_6")
        # myElem_7 = (
        #     WebDriverWait(browser, 10)
        #     .until(
        #         EC.element_to_be_clickable(
        #             (By.CLASS_NAME, "div.item  selected")
        #         )
        #     )
        #     .click()
        # )
        # print("myElem_7")
        # sleep(10)
        # myElem_8 = (
        #     WebDriverWait(browser, 10)
        #     .until(
        #         EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'ค้นหา')]"))
        #     )
        #     .click()
        # )
        # print("myElem_8")
        # sleep(10)

        # soup = BeautifulSoup(browser.page_source, "lxml")
        # myElem_4 = WebDriverWait(browser, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "input.resizable-input"))
        # )
        # myElem_4.send_keys("DENSO ")
        # # myElem_4.click()
        # myElem_5 = (
        #     WebDriverWait(browser, 10)
        #     .until(
        #         EC.element_to_be_clickable(
        #             (By.CSS_SELECTOR, "button.c165.c413.c420.c285")
        #         )
        #     )
        #     .click()
        # )
        # myElem_6 = (
        #     WebDriverWait(browser, 10)
        #     .until(
        #         EC.element_to_be_clickable(
        #             (By.XPATH, "//*[contains(text(), 'เข้าสู่ระบบ')]")
        #         )
        #     )
        #     .click()
        # )

        sleep(50)
        print("Completed!")
        # browser.close()
    except TimeoutException:
        print("No element found")
    sleep(5)
    browser.close()
