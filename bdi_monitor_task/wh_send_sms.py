#!/usr/bin/env python
# -*-coding:utf-8 -*-
#********************************************************************************
# 文件名称：run.py
# 功能描述：华为任务监控
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20191020
# 修改日志：20191226
# 修改日期：
# ****************************************************************************
# 程序调用格式：nohup python run_wh.py >> nohup.out &
# *******************************************************************************

import os
import sys
import time
#import config
#import bdi_monitor_task


# 启动
if __name__=='__main__':
	
	
	#input_length = len(sys.argv)
	#print 'input_str: ',len(sys.argv)
	#
	## 1.默认监控HBASE集群:1代表HBASE集群，2代表三期集群
	#monitor_server=1
	#if input_length == 2 and sys.argv[1]=='2':
	#	
	#	monitor_server=2

	while True:
	
		# 1.监控各类服务
		#service_monitor_object = service_monitor.ServiceMonitor(monitor_server)
		#service_monitor_object.request_data()
		#
		## 2.监控solr
		## 三期集群不监控solr
		#if monitor_server==1:
		#	solr_monitor_object = solr_monitor.SolrMonitor()
		#	solr_monitor_object.request_data()
		#
		## 3.监控kafka消费
		#
		## 4.监控kafka日志，有监控
		#
		#print('sleep 900s')
		#time.sleep(config.sleep_time)
		
		#bdi_monitor_task.create_running()
		
		run_sh='sh trans_data_bdi2sanqi.sh dw_locl_wh_lacci_4g_time_tmp_yyyymmdd 20200109 dw_locl_wh_lacci_4g_time_tmp_yyyymmdd'
		
		os.popen(run_sh).readlines()
		
		# 休息10分钟，600
		
		print 'sleep 10s'
		time.sleep(60)

