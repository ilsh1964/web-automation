#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://ilsh.duckdns.org')

try:
    # We will wait up to 10 seconds for the page loading process
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "2021")))
    element.click()
except:
    driver.quit()

time.sleep(20)
