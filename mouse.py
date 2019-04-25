#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: palmer.lu
# @license: (C) Copyright 2018-2019.
# @contact: luxingp@qq.com
# @software: LearnBySelf
# @file: mouse.py
# @time: 4/18/2019 2:54 PM


from selenium import webdriver
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('http://yunpan.360.cn')

#1 context_click()
#定位到要右击的元素
right_click = driver.find_element_by_id('xx')
#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()

#2 move_to_element()
#定位到要悬停的元素
above = driver.find_element_by_id('id')
#对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()

#3 double_click()
#定位到要悬停的元素
double_click = driver.find_element_by_id('xx')
#对定位到的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()


#4 drag_and_drop(source,target)
# souce: 鼠标拖动的源元素
# target:鼠标释放的目标元素
#定位元素的原位置
element = driver.find_element_by_id('xx')
#定位元素要移动到的目标位置
target = driver.find_element_by_id('xx')
#执行元素的拖放操作
ActionChains(driver).drag_and_drop(element,target).perform()
