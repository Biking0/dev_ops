#!/usr/bin/env python
# -*-coding:utf-8 -*-
#********************************************************************************
# 文件名称：run.py
# 功能描述：华为任务监控
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20200318
# 修改日志：
# 修改日期：
# ****************************************************************************
# 程序调用格式：nohup python run_65.py >> nohup.out &
# *******************************************************************************

import os
import sys
import time


# 启动
if __name__=='__main__':	
	

	while True:	
		
		run_sh='sh scp_file_server.sh >> nohup.out'
		
		os.popen(run_sh).readlines()
		
		# 休息10分钟，600
		
		print 'sleep 24h'
		time.sleep(86400)

