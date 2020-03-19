#!/usr/bin/env python
# -*-coding:utf-8 -*-
# *******************************************************************************
# �ļ����ƣ�timestamp2format_tool.py
# ����������ʱ������ʽ��ʱ���໥ת������
# �� �� ��10041 20191015100000 20191015110000
# �� �� �� 
# �� �� �ߣ�hyn
# �������ڣ�20191015
# �޸���־���໥ת��
# �޸����ڣ�20191104
# ***************************************************************************
# ������ø�ʽ��
# 1.����ʱ���ת��Ϊ��ʽ��ʱ�䣺python timestamp2format_tool.py 1572920510000
# 2.�����ʽ��ʱ��ת��Ϊʱ�����������ʱ�֣���python timestamp2format_tool.py 201910151730
# 3.û�в���Ĭ�������ǰʱ�䣺python timestamp2format_tool.py
# *******************************************************************************

import sys
import time

# ʱ���ת��Ϊ��ʽ��ʱ��
def timestamp2format_tool(timestamp):

	# ��ȡ����
	timestamp = timestamp[0:-3]
	
	formattime= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(timestamp)))
	print formattime
	return formattime
	
# ��ʽ��ʱ��ת��Ϊʱ���
def format2timestamp_tool(input_str):
	print str(time.mktime(time.strptime(input_str,'%Y%m%d%H%M'))).split('.')[0]+'000'
	
def get_localtime():
	local_timestamp=str(time.time()).split('.')[0]+'000'
	local_formattime=timestamp2format_tool(local_timestamp)
	print '��ǰʱ�����',local_timestamp
	print '��ǰʱ�䣺',local_formattime
	
# ����
if __name__=='__main__':	
	
	print '# 1.python timestamp2format_tool.py 1572920510000 ��ʱ���ת��Ϊ��ʽ��ʱ�䣩'
	print '# 2.python timestamp2format_tool.py 201910151730 ����ʽ��ʱ��ת��Ϊʱ�����������ʱ�֣���'
	print '# 3.python timestamp2format_tool.py ��û�в���Ĭ�������ǰʱ�䣩'
	
	input_str=sys.argv[0]
	input_length = len(sys.argv)
	
	# û�в���Ĭ�������ǰʱ��
	if input_length == 1:
		get_localtime()
		exit()
	
	try :
		input_str=sys.argv[1]
		
		print 'input:',input_str[0:2]
	except:
		print 'input error !'
		exit()
	
	# ����Ϊʱ���
	if input_str[0:2]=='15':
		timestamp2format_tool(input_str)
		
	
	# ����Ϊ��ʽ��ʱ��
	elif input_str[0:2]=='20':
		format2timestamp_tool(input_str)
	
	else :
		print 'input error !'
		exit()
		
		
		