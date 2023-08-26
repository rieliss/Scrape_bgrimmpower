# importing required package of webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # Instantiate the webdriver with the executable location of MS Edge
    # browser = webdriver.Edge(r"msedgedriver.exe")
    # browser = webdriver.Edge(
    #     r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    # )
    edgeService = Service(r"D:\\Lambdatest Tools\\edgedriver_win64\\msedgedriver.exe")
    browser = webdriver.Edge(service=edgeService)
    # Simply just open a new Edge browser and go to lambdatest.com
    browser.maximize_window()
    browser.get("https://amr.pttngd.co.th/")
    try:
        myElem_1 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        myElem_1.send_keys("AMNDENSO")
        myElem_1.click()
        myElem_2 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        myElem_2.send_keys("on566")
        myElem_2.click()
        myElem_3 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.c165.c151.c158"))
            )
            .click()
        )
        myElem_4 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.resizable-input"))
        )
        myElem_4.send_keys("DENSO ")
        # myElem_4.click()
        myElem_5 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.c165.c413.c420.c285")
                )
            )
            .click()
        )
        myElem_6 = (
            WebDriverWait(browser, 10)
            .until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), 'Export')]")
                )
            )
            .click()
        )
        # sleep(50)

        print("Completed!")
        browser.close()
    except TimeoutException:
        print("No element found")
    sleep(10)
    browser.close()
