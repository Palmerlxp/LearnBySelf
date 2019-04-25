#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: palmer.lu
# @license: (C) Copyright 2018-2019.
# @contact: luxingp@qq.com
# @software: LearnBySelf
# @file: wait.py
# @time: 4/18/2019 3:32 PM

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'KW')))

element.send_keys('semenium')
driver.quit()

