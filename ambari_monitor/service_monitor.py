#!/usr/bin/env python
# -*-coding:utf-8 -*-
# *******************************************************************************
# �ļ����ƣ�service_monitor.py
# �����������������ͨ�ü��
# �� �� �� 
# �� �� �� 
# �� �� �ߣ�hyn
# �������ڣ�20191010
# �޸���־��
# �޸����ڣ�20191229
# *******************************************************************************
# ������ø�ʽ��python service_monitor.py
# *******************************************************************************

import os
import sys
import json
import time
import config

# �����ṹ���:
# 1.��ʼ��
# 2.��������
# 3.�������ݱ༭
# 4.���Ͷ���

class ServiceMonitor():
	
	# ��ʼ��
	def __init__(self,monitor_server):
		
		# ��������
		self.sms_list=[]
		self.monitor_server=monitor_server
		self.monitor_url=config.monitor_url
		self.monitor_name=config.monitor_name
		self.log_name=config.hbase_service_monitor
		
		if monitor_server==2 :
			self.monitor_url=config.sanqi_url
			self.monitor_name=config.sanqi_name
			self.log_name=config.sanqi_service_monitor
		print '��ʼ����',self.monitor_server
		
	# ��������
	def request_data(self):
		
		# ѭ������������
		for service_name in config.service_list:
		
			# �������״̬�������������txt�ļ�
			exec_sh = 'curl -u admin:admin '+self.monitor_url+'/'+self.monitor_name+'/services/'+service_name+' > '+config.log_path+self.log_name+'.txt'
			# print 'exec_sh: '+exec_sh
			result_data = os.popen(exec_sh).readlines()
			
			try:
			
				self.sms_info(service_name,result_data)
			except Exception as e:
				print '# monitor '+service_name +'error,next'
				print e
				continue
	
	# �������ݱ༭
	def sms_info(self,service_name,result_data):
	
		# ��ȡkafka�����ļ���Ϣ
		f=open(config.log_path+self.log_name+'.txt')
		dict_data=json.load(f)

		# service��Ⱥ��Ϣ
		service_info=dict_data['alerts_summary']
		critical_info=service_info['CRITICAL']
		host_info=service_info['OK']
		host_count=len(dict_data['alerts'])
		
		# hbase��Ⱥ������Ϣ
		#HDFS_number=1
		# hbase��Ⱥ������Ϣ�����Ծ�����Ϣ��20200102
		HDFS_number=7
		YARN_number=0
		
		if service_name=='HDFS' and self.monitor_server==1:
			host_count=host_count-30
		# HBASE��Ⱥ
		if service_name=='YARN' and self.monitor_server==1:
			host_count=host_count-2
			YARN_number=2
		
		# ���ڼ�Ⱥ
		if service_name=='HDFS' and self.monitor_server==2:
			host_count=host_count-64
			
			# ���ڼ�Ⱥ������Ϣ
			HDFS_number=63
		print service_name+'��������������'+str(host_count)
		
		#HDFS_number=0
		
		# �������ݱ༭����Ӽ�Ⱥ����
		server_name_CH=config.hbase_name_CH
		
		if self.monitor_server==2:
			server_name_CH=config.sanqi_name_CH
			#print '��Ⱥ��������',server_name_CH
		
		# ����HDFS��Ч����
		if service_name=='HDFS':
			#if critical_info>-1:
			
			# test
			print 'critical_info1',critical_info
			
			if critical_info>HDFS_number:
				critical_sms_info=server_name_CH+service_name+'����'+str(critical_info)+'��������ϢCRITICAL��'
				self.sms_list.append(critical_sms_info)
				print critical_sms_info
			
			# �����������
			#if host_info<host_count+1:
			if host_info<host_count:
				host_sms_info=server_name_CH+service_name+'��������������������'+str(host_count)+'����'+str(host_info)
				self.sms_list.append(host_sms_info)
				print host_sms_info
		
		elif service_name=='YARN':
			#if critical_info>-1:
			
			# test
			print 'critical_info2',critical_info
			
			if critical_info>YARN_number:
				critical_sms_info=server_name_CH+service_name+'����'+str(critical_info)+'��������ϢCRITICAL��'
				self.sms_list.append(critical_sms_info)
				print critical_sms_info
			
			# �����������
			#if host_info<host_count+1:
			if host_info<host_count:
				host_sms_info=server_name_CH+service_name+'��������������������'+str(host_count)+'����'+str(host_info)
				self.sms_list.append(host_sms_info)
				print host_sms_info
			
		else:
			# test
			print 'critical_info3',critical_info
			
			#if critical_info>-1:
			if critical_info>0:
				critical_sms_info=server_name_CH+service_name+'����'+str(critical_info)+'��������ϢCRITICAL��'
				self.sms_list.append(critical_sms_info)
				print critical_sms_info
			
			# �����������
			#if host_info<host_count+1:
			if host_info<host_count:
				host_sms_info=server_name_CH+service_name+'��������������������'+str(host_count)+'����'+str(host_info)
				self.sms_list.append(host_sms_info)
				print host_sms_info
		
		# ���Ͷ���
		if config.send_flag:
			self.send_sms(service_name)
	
	# ���Ͷ���
	def send_sms(self,service_name):
		
		for sms_info in self.sms_list:
			
			# ���Ͷ���
			os.popen('sh send_sms.sh'+' '+sms_info+' '+config.all_info).readlines()
			# ����������д����־
			os.popen('echo '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' '+sms_info+' >> '+config.log_path+self.log_name+'.log').readlines()
			
			print service_name+' ���ţ�'+sms_info
		
		# �����Ϣ�б�
		self.sms_list=[]

# ��������
#if __name__=='__main__':
#	sm = ServiceMonitor()
#	
#	while True:
#		sm.request_data()
#		time.sleep(config.sleep_time)
#	
#	
