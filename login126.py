#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: palmer.lu
# @license: (C) Copyright 2018-2019.
# @contact: luxingp@qq.com
# @software: LearnBySelf
# @file: login126.py
# @time: 4/18/2019 11:32 AM

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.126.com')

driver.find_element_by_id('idInput').clear()
driver.find_element_by_id('idInput').send_keys('username')
driver.find_element_by_id('pwdInput').clear()
driver.find_element_by_id('pwdInput').send_keys('password')
driver.find_element_by_id('loginBtn').click()

driver.quit()


