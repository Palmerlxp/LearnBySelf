#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: palmer.lu
# @license: (C) Copyright 2018-2019.
# @contact: luxingp@qq.com
# @software: LearnBySelf
# @file: checkbox.py.py
# @time: 4/19/2019 4:19 PM
from selenium import webdriver
import os
import time

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

#通过XPath找到type=checkbox的元素
#checkboxes = driver.find_element_by_xpath('//input[@type='checkbox']')

#通过CSS找到type=checkbox的元素
checkboxes = driver.find_element_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)

#打印当前页面上type为checkbox的个数
print(len(checkboxes))


#把页面上最后1个checkbox的钩给去掉
driver.find_element_by_css_selector('input[type=checkbox]').pop().click()

driver.quit()

