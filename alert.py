#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: palmer.lu
# @license: (C) Copyright 2018-2019.
# @contact: luxingp@qq.com
# @software: LearnBySelf
# @file: alert.py
# @time: 4/22/2019 11:37 AM


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#鼠标悬停至‘设置’链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()

#保存设置
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)

#接受警告框
driver.switch_to.alert().accept()



driver.quit()

