#!/usr/bin/env python
# -*-coding:utf-8 -*-
# *******************************************************************************
# * �ļ����ƣ�search_solr_tool.py
# * ����������solr��ѯ���ߣ���ѯʱ������Ƿ�����
# * �� �� ��10041 20191015100000 20191015110000
# * �� �� �� 
# * �� �� �ߣ�hyn
# * �������ڣ�20191015
# * �޸���־��������id
# * �޸����ڣ�20200127
# *****************************************************************************
# * ������ø�ʽ��
# * 1.Ĭ�ϲ�ѯ30���ӣ�                                                                          python search_solr_tool.py
# * 2.��ѯָ������ʱ����5���ӣ�:                                                        python search_solr_tool.py 5
# * 3.��ѯָ���id��ָ������ʱ��                                                      python search_solr_tool.py 10678 5
# * 5.��ѯָ���id��ָ����ʼʱ�����ʱ�䣬ʱ�侫ȷ���룺      py search_solr_tool.py 10678 20191025220400 20191025223400
# *******************************************************************************

import os
import sys
import time
import json
import datetime
# import config

# Ĭ�ϲ�ѯ����30����
search_time=30

# Ĭ��activity_num
# 10601 10061 10678 10221 10730
default_activity_num = '10061'

# ��ѯsolr
def search_solr(activity_num,start_time_stamp,end_time_stamp):

        # ��ѯsolr����������search_solr.txt
        solr_sh='curl -i -H "Content-Type:application/json" -X POST --data \''+'{"condition":"activity_num:'+activity_num+' AND start_time:{\\"'+start_time_stamp+'\\" TO \\"'+end_time_stamp+'\\"}" ,"tables":["DW_LOC_ZX_USER_BH_MIN_20200210"],"query":"","start":0,"return_fields":["phone","imsi","start_time","city_id","county_id"],"cursor_mark":"*","sort":"id desc","rows":10000}\' '+'http://10.218.146.65:9000/ocsearch-service/query/search | more'+' > search_solr.txt'

        print solr_sh

        result=os.popen(solr_sh).readlines()

        # ��ȡ�����ļ���Ϣ
        f=open('search_solr.txt').readlines()

        dict_data=json.loads(f[6])

        # ��ӡ��ѯ�����������ʹ��
        #print f

        print '���ƻid,solr����'+str(search_time)+'������������'+str(dict_data['data']['total'])

# ��ѯsolr
def search_solr_allid(activity_num,start_time_stamp,end_time_stamp):

        # ��ѯsolr����������search_solr.txt
        solr_sh='curl -i -H "Content-Type:application/json" -X POST --data \''+'{"condition":"start_time:{\\"'+start_time_stamp+'\\" TO \\"'+end_time_stamp+'\\"}" ,"tables":["DW_LOC_ZX_USER_BH_MIN_20200210"],"query":"","start":0,"return_fields":["phone","imsi","start_time","city_id","county_id"],"cursor_mark":"*","sort":"id desc","rows":10000}\' '+'http://10.218.146.65:9000/ocsearch-service/query/search | more'+' > search_solr.txt'

        print solr_sh

        result=os.popen(solr_sh).readlines()

        # ��ȡ�����ļ���Ϣ
        f=open('search_solr.txt').readlines()

        dict_data=json.loads(f[6])

        # ��ӡ��ѯ�����������ʹ��
        #print f

        print 'solr����'+str(search_time)+'��������������'+str(dict_data['data']['total'])


# ����
if __name__=='__main__':

        print '# 1.python search_solr_tool.py (Ĭ�ϲ�ѯ30����)'
        print '# 2.python search_solr_tool.py 5 (��ѯָ������ʱ��,5���ӣ�)'
        print '# 3.python search_solr_tool.py 10601 5 (��ѯָ���id��ָ������ʱ��)'
        print '# 4.py search_solr_tool.py 10601 20191025220400 20191025223400 (��ѯָ���id��ָ����ʼʱ�����ʱ�䣬ʱ�侫ȷ����)'

        input_str=sys.argv[0]
        input_length = len(sys.argv)
        print 'input_str: ',input_str,len(sys.argv)


        # �����ѯ����
        activity_num= default_activity_num
        # ת��Ϊʱ���
        end_time_stamp = str(time.time()).split('.')[0]
        start_time_stamp = str(int(end_time_stamp)-search_time*60)

        # if len(sys.argv)

        # 1.Ĭ�ϲ�ѯ30����
        if input_length == 1:

                pass

        # 2.��ѯָ������ʱ��
        if input_length == 2:
                search_time=int(sys.argv[1])
                end_time_stamp = str(time.time()).split('.')[0]
                start_time_stamp = str(int(end_time_stamp)-search_time*60)


        # 3.��ѯָ���id��ָ������ʱ��
        if input_length == 3:
                search_time=int(sys.argv[2])
                activity_num=sys.argv[1]
                end_time_stamp = str(time.time()).split('.')[0]
                start_time_stamp = str(int(end_time_stamp)-search_time*60)

        # 4.��ѯָ���id��ָ����ʼʱ�����ʱ��
        if input_length == 4:

                activity_num=sys.argv[1]
                start_time = sys.argv[2]
                end_time = sys.argv[3]

                # ���ü�3��000
                #start_time_stamp=str(time.mktime(time.strptime(start_time,'%Y%m%d%H%M%S'))).split('.')[0]+'000'
                #end_time_stamp=str(time.mktime(time.strptime(end_time,'%Y%m%d%H%M%S'))).split('.')[0]+'000'
                start_time_stamp=str(time.mktime(time.strptime(start_time,'%Y%m%d%H%M%S'))).split('.')[0]
                end_time_stamp=str(time.mktime(time.strptime(end_time,'%Y%m%d%H%M%S'))).split('.')[0]

        print '��ѯ����: ',activity_num,start_time_stamp,end_time_stamp

        # ��ѯsolr
        search_solr(activity_num,start_time_stamp,end_time_stamp)
        search_solr_allid(activity_num,start_time_stamp,end_time_stamp)


