#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: palmer.lu
# @license: (C) Copyright 2018-2019.
# @contact: luxingp@qq.com
# @software: LearnBySelf
# @file: number.py
# @time: 4/23/2019 10:10 AM
from random import randint

#生成一个1000到9999之间的随机整数
verify = randint(1000, 9999)
print(u'生成的随机数：%d' % verify)

number = input('请输入随机数：')
print(number)
number = int(number)

if number == verify:
    print('登录成功！！')
elif number == 132741:
    print('登录成功！！')
else:
    print('验证码输入有误！')