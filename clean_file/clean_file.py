#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：clean_file.py
# 功能描述：clean 60 days ago log
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20200202
# 修改日志：
# 修改日期：20200309
# ***************************************************************************
# 程序调用格式：python clean_file.py
# ***************************************************************************

import os
import sys
import time

#path="./"

#delete 2 day ago file
day=7

log_path='./log/'

delete_time=time.time()-3600*24*day

path_list=['/var/log/hadoop-yarn/ocdp/','/var/log/hadoop/ocdp','/var/log/hbase','/var/log/kafka']
#'/home/ocdp/javaApp/zx_core_tomcat/logs','/data/javaAppLogs/zx_core','/home/ocdp/javaApp/zj_interface_apache-tomcat-7.0.73/logs','/data/javaAppLogs/zj_interface','/home/ocdp/javaApp/zj_task2_apache-tomcat-7.0.73/logs','/data/javaAppLogs/zx_task','/home/ocdp/javaApp/zx_web_tomcat/logs','/data/javaAppLogs/zj_web','/data']



for path in path_list:
	try:
		for file in os.listdir(path):
				filename=path+os.sep+file
		
				if os.path.getmtime(filename)< delete_time:
						os.remove(filename)
						print filename+" is removed"
						
	except:
		continue