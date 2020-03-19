#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：cpu_monitor.py
# 功能描述：
# 1.监控华为yarn资源
# 2.监控119、120主机硬盘空间
# 功能描述：
# 功能描述：
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20191023
# 修改日志：
# 修改日期：
# ***************************************************************************
# 程序调用格式：python cpu_monitor.py
# ***************************************************************************

# 方法结构：
# 生成查询结果



import os
import sys
import time
import json
import datetime

f=open('yarn_top.txt').readlines()

print f
print type(f)
print len(f)
print '################'
print f[0]
print f[1]
print f[2]
print type(f[2])
result_list = f[1].split(' ')
print result_list
print result_list[0]
print result_list[4]

for i in result_list:
	if i == '' or i == ' ':
		result_list.remove(i)

print result_list
print result_list[0]

if result_list[0] == 'application_1572454954315_6153375':
	print 'yes'

if result_list[0] == '\x1b[27m\x1b[Kapplication_1572454954315_6153375':
	print 'yess'
print result_list[4]
