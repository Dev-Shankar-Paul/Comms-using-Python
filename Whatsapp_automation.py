#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:19:07 2020

@author: dsp
"""
# SENDING WHATSAPP MESSAGE USING SELENIUM

"""
==============
OUTDATED CODE
==============

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

location = '/home/dsp/Downloads/chromedriver_linux64/chromedriver'

driver = webdriver.Chrome(location)

driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)

chrome_options = webdriver.ChromeOptions() 
chrome_options.add_experimental_option("excludeSwitches",
                                       ['enable-automation'])
driver = webdriver.Chrome(location, options=chrome_options) 
driver.get('https://web.whatsapp.com/')
#wait = WebDriverWait(driver, 600)
time.sleep(10)

target = 'Big Bro'

message = 'Hello'

x_arg = '//span[contains(@title,'+ target +')]'
group_title = ec.presence_of_element_located((By.XPATH, x_arg))
group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = ec.presence_of_element_located((By.XPATH, inp_xpath))
for i in range(0, 5):
    input_box.send_keys(message + Keys.ENTER) 
    time.sleep(1)

"""
"""
=========
NEW CODE
=========
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

location = '/home/dsp/Downloads/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(location)
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the user : ')
msg = input('Enter your message : ')
count = input('Enter the number of times you want to send message : ')

input('Enter something after scanning QR Code....')

element =  driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
actions = ActionChains(driver)
actions.move_to_element(element).perform()

element.click()

inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
input_box.click()

for i in range(0, int(count)):
    input_box.send_keys(msg + Keys.ENTER)
    time.sleep(1)

