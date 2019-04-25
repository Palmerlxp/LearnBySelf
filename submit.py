#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: palmer.lu
# @license: (C) Copyright 2018-2019.
# @contact: luxingp@qq.com
# @software: LearnBySelf
# @file: submit.py
# @time: 4/18/2019 2:11 PM
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.youdao.com')

driver.find_element_by_id('query').send_keys('hello')
#提交输入框的内容
driver.find_element_by_id('query').submit()

driver.quit()




