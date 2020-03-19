bdi@HACC-BH02-SERVICE118:~/hyn/hive_table_check> cat bak_trans_data_bdi2sanqi_chk.sh  
#!/bin/bash
# ***************************************************************************
# �ļ����ƣ�trans_data_bdi2sanqi_chk.sh
# �����������ձ�����У���ļ���������ƽ̨hdfs����ͬ��������hdfs��Ⱥ�������±��ձ�Сʱ��
# �� �� ��
# �� �� ��
# �� �� �ߣ�hyn
# �������ڣ�20191216
# �޸���־��
# �޸����ڣ�
# ***************************************************************************
# ������ø�ʽ��sh trans_data_bdi2sanqi_chk.sh table_name data_time running_num
# ***************************************************************************

# ��Ϊ��������֤
source /opt/fi_client/bigdata_env
kinit -kt /home/bdi/user.keytab asiainfouser1

# �����������
table_name=$1
data_time=$2
running_num=$3
echo ${running_num} > ${table_name}_${data_time}.txt

# ����У���ļ�
# hadoop fs -touchz /asiainfo/dependent/${table_name}_${data_time}.txt
# hadoop fs -put /asiainfo/dependent/${table_name}_${data_time}.txt
hadoop fs -put ./${table_name}_${data_time}.txt /asiainfo/dependent/
