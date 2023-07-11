#!/usr/bin/env python3
# sudo apt install python3-pip
# pip install sellenium
import time
from selenium import webdriver

web = webdriver.Chrome()
web.get('https://login.bankhapoalim.co.il')
time.sleep(3)

username = 'UUUUUUUU'   # Change It
username_xpath = web.find_element('xpath', '//*[@id="userCode"]')
username_xpath.send_keys(username)

passwd = 'PPPPPPPP'    # Change it
passwd_xpath = web.find_element('xpath', '//*[@id="password"]')
passwd_xpath.send_keys(passwd)


submit = web.find_element('xpath', '/html/body/auth-root/auth-rb-login/div/div[2]/div[1]/div/form/fieldset/div[3]/button')
submit.click()
time.sleep(180)

