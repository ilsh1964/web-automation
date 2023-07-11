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
    EC.presence_of_element_located((By.ID, "search-form-1")))

    search_xpath = driver.find_element('xpath', '//*[@id="search-form-1"]')
    search_xpath.clear() # clear the textbox
    search_xpath.send_keys("docker")
    search_xpath.send_keys(Keys.RETURN)
    time.sleep(20)
except:
    time.sleep(20)
    driver.quit()

time.sleep(20)
