#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: palmer.lu
# @license: (C) Copyright 2018-2019.
# @contact: luxingp@qq.com
# @software: LearnBySelf
# @file: take_screenshot.py
# @time: 4/22/2019 5:07 PM

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

#截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file('C:\pyscreenshot\ baidu_img.jpg')

driver.quit()
