# encoding=utf8
# Scheduled to run on Friday
# ��ʱÿ��������
# by hyn
# ���з�ʽ��nohup python schedule_run.py >> /home/ocetl/hyn/miguread/log/schedule_run.log
# 20200220

import os
import time
import datetime


def run():
    pass


log_path = '/home/ocetl/hyn/miguread/log/'

while True:
    # ������ָ��ʱ������
    today = datetime.datetime.now().weekday() + 1
    print today

    # ���嵱��ÿСʱ����Ƿ�15���Ժ󣬷�����ÿ5��Сʱ���һ��
    if today == 5:
        while True:

            # ��ȡ���嵱��15��ʱ��
            today_str = time.strftime('%Y%m%d', time.localtime(time.time()))

            is_runed= '/home/ocetl/hyn/miguread/log/migureading_running_' + today_str + '.log'
            print is_runed

            # �Ƿ����й�
            if os.path.exists(is_runed):
                # ��Ϣ24Сʱ
                print datetime.datetime.now()
                print 'is_runed sleep 24hour'
                time.sleep(86400)

                # ִ��������˳�
                break

            stamptime_15 = time.mktime(time.strptime(today_str + ' 15:00:00', '%Y%m%d %H:%M:%S'))

            # ��ȡ��ǰʱ���
            stamptime_now = time.time()

            # �Ƿ񵽵���15���Ժ�
            print stamptime_15
            print stamptime_now

            if stamptime_now > stamptime_15:
                print 'start run'

                # ���ó���,python sh
                # python /home/ocetl/yfx/migureading_running.py 20200207
                # sh /home/ocetl/yfx/recommend/six.sh kf_01_mass_cmread_rec_2020_week5_1_six_20200207 20200207
                # sh /home/ocetl/yfx/recommend/ten.sh kf_01_mass_cmread_rec_2020_week5_1_20200207 20200207
                python_sh = 'nohup python /home/ocetl/yfx/migureading_running.py' + ' ' + today_str + ' > /home/ocetl/hyn/miguread/log/migureading_running_' + today_str + '.log'
                six_sh = 'nohup sh /home/ocetl/yfx/recommend/six.sh kf_01_mass_cmread_rec_2020_week5_1_six_' + today_str + ' ' + today_str + ' > /home/ocetl/hyn/miguread/log/six_' + today_str + '.log'
                ten_sh = 'nohup sh /home/ocetl/yfx/recommend/ten.sh kf_01_mass_cmread_rec_2020_week5_1_' + today_str + ' ' + today_str + ' > /home/ocetl/hyn/miguread/log/ten_' + today_str + '.log'

                print python_sh
                print six_sh
                print ten_sh

                # ����
                # python1_sh = 'nohup python /home/ocetl/hyn/test/sleep.py > python1_sh.log'
                # sh1 = 'nohup sh /home/ocetl/hyn/test/sleep.sh > sh1.log'
                # sh2 = 'nohup sh /home/ocetl/hyn/test/sleep2.sh > sh2.log'
                # print python1_sh
                # os.popen(python1_sh)
                # print sh1
                # os.popen(sh1)
                # print sh2
                # os.popen(sh2)

                # ִ�нű�

                # ִ������
                print python_sh
                os.popen(python_sh)
                print six_sh
                os.popen(six_sh)
                print ten_sh
                os.popen(ten_sh)

                # ��Ϣ24Сʱ
                print datetime.datetime.now()
                print 'sleep 24hour'
                time.sleep(86400)

                # ִ��������˳�
                break

            print 'sleep 30min'
            time.sleep(1800)
    print datetime.datetime.now()
    print '���������'
    print 'sleep 5hour'
    time.sleep(18000)


# week = datetime.datetime.strptime("20200220", "%Y%m%d").weekday() + 1
# print week

