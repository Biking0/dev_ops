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

import os
import sys
import time
import json
import datetime

result_list=[]

def search_yarn():
	
	# yarn资源信息
	search_yarn_sh='yarn top > yarn_top.txt'
	
	# 标识文件
	os.popen('touch yarn_top.chk').readlines()
	
	
	#os.popen(search_yarn_sh).readlines()
	
	os.system(search_yarn_sh)
	
	os._exit(-1)
	
	print '##############'
	
	
	
	# 执行 yarn top
	#os.popen(search_yarn_sh).readlines()
	yarn_info()
	
def yarn_info():
	
	f=open('yarn_top.txt').readlines()
	
	# 每行数据放到list，不要首行
	for i in range(1,len(f)):
		result_str_list=f[i].split(' ')
		
		# 去除空格
		for j in result_str_list:
			if j == '' or j == ' ' or j == '  ':
				result_str_list.remove(j)
		
		result_list.append(result_str_list)
	
	print '# result_list',result_list

search_yarn()
