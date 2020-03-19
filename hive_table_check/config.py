bdi@HACC-BH02-SERVICE118:~/hyn/hive_table_check> cat config.py
# encoding=utf-8
# hive_table_check
# by hyn
# 20200224

# hadoop path
bdi_hadoop_path='hadoop fs -du -s -h  /user/hive/warehouse/asiainfoh.db/'

# table_name_list
# 表名，允许延迟时长
hour_table=[
['dw_locl_wh_lacci_4g_time_yyyymmddhh',2]
]

day_table=[
['table_name',1]
]
