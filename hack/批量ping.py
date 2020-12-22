# coding=utf-8
import os
import threading

areas = ['www.baidu.com', 'testingedu.com.cn', 'ke.qq.com']


def run_cmd(a):
    cmd = 'ping ' + a
    os.system(cmd)


for a in areas:
    th1 = threading.Thread(target=run_cmd, args=(a,))
    # 线程开始执行
    th1.start()
