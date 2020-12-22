# coding=utf-8
import os
import time

import psutil
from time import sleep
from socket import *
import requests
import json
import dns.resolver


# 字节转换
def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    # 列举
    for i, s in enumerate(symbols):
        prefix[s] = 1024 ** (i + 1)  # k=1024
    #     颠倒 从大到小
    for s in reversed(symbols):
        if n >= prefix[s]:  # 如果1024>=1024
            value = n / prefix[s]  # 1024/1024
            return '%.1f%s' % (value, s)
    return '%sB' % n


# 获取cpu信息
def get_cpu(t):
    info = 'CPU使用率：%.2f' % psutil.cpu_percent(interval=1)
    return str(info) + '%\n'


# 获取内存信息
def get_memory():
    var = psutil.virtual_memory()
    info = '总大小：%s\n已使用的：%s\n空闲的：%s\n使用百分比：%s\n' % (
        bytes2human(var.total),
        bytes2human(var.used),
        bytes2human(var.free),
        str(var.percent) + '%'
    )
    return info


# 交换分区
def get_smemory():
    var = psutil.swap_memory()
    info = '交换分区信息：\n总大小：%s\n已使用的：%s\n空闲的：%s\n使用百分比：%s\n' \
           '调入swap分区数据大小：%s\n从swap分区调出的数据大小：%s\n' \
           % (
               bytes2human(var.total),
               bytes2human(var.used),
               bytes2human(var.free),
               str(var.percent) + '%',
               bytes2human(var.sin),
               bytes2human(var.sout)
           )
    return info


# 获取磁盘信息
def get_disk_use():
    # psutil.disk_partitions() 查看所有磁盘
    var = psutil.disk_usage('c:\\')
    info = '磁盘信息：\n总大小：%s\n已使用：：%s\n空闲的：%s\n使用百分比：%s\n' % (
        bytes2human(var.total),
        bytes2human(var.used),
        bytes2human(var.free),
        var.percent
    )
    return info


# 磁盘读写
def get_disk_io():
    t1 = psutil.disk_io_counters()
    sleep(1)
    t2 = psutil.disk_io_counters()
    info = '磁盘IO信息：\nRead/s：%s\nWrite/s：%s\nTps/s：%s\n' % (
        bytes2human(t2.read_bytes - t1.read_bytes),
        bytes2human(t2.write_bytes - t1.write_bytes),
        (t2.read_count + t2.write_count) - (t1.read_count + t1.write_count)
    )
    return info


def main():
    func_dict = {'cpu': get_cpu, 'memory': get_memory, 'disk': get_disk_use, 'disk_io': get_disk_io}
    s_sock = socket(AF_INET, SOCK_STREAM)  # tcp/ipv4
    s_sock.bind(('0.0.0.0', 8000))
    s_sock.listen(5)
    print('Wait For Connection...')
    while True:
        c_sock, c_addr = s_sock.accept()  # 接收这个用户连接
        print('Connection From：', c_addr)
        while True:
            data = c_sock.recv(1024).decode('utf-8')  # 获取客户端发送过来的数据
            if not data:
                print("Connection Close：", c_addr)
                break
            func = func_dict.get(data)
            if func:
                buf = func().encode('utf-8')
                c_sock.send(buf)
            else:
                buf = '无效的信息获取'.encode('utf-8')
                c_sock.send(buf)
        c_sock.close()
    # s_sock.close()


def get_process():
    time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    monitor_name = {'httpd'}
    # 要监控的服务名集合
    monitor_map = {
        'httpd': 'service httpd start'
    }
    proc_dict = {}
    # id:进程名
    proc_name = set()
    for p in psutil.process_iter(attrs=['pid', 'name']):
        proc_dict[p.info['pid']] = p.info['name']
        proc_name.add(p.info['name'])
    # print(proc_dict)
    # print(proc_name)
    # 提取出来哪个进程没有在当前操作系统下开启
    proc_stop = monitor_name - proc_name
    print(proc_stop)
    if proc_stop:
        # 取出所有没有启动的进程集合
        for p in proc_stop:
            p_status = '停止'
            p_name = p
            os.system(monitor_map[p])
            proc_name = set()
            for p in psutil.process_iter(attrs=['pid', 'name']):
                proc_name.add(p.info['name'])
            if p in proc_name:
                p_status = '启动'


def dns_analysis_ip(domain_name):
    A = dns.resolver.resolve(domain_name, 'A')
    for i in A.response.answer:
        print(f'A记录：', i)
    try:
        B = dns.resolver.query(domain_name, 'MX')
        for j in B:
            print(f'MX记录：',j)
    except dns.resolver.NoAnswer:
        print('没有MX记录')
    C = dns.resolver.query(domain_name, 'CNAME')
    for c in C:
        print(f'CNAME记录：', c)


if __name__ == '__main__':
    # while True:
    #     sleep(1)
    #     print(get_cpu(1))
    #     # print(get_memory())
    #     # print(get_smemory())
    #     # print(get_disk_use())
    #     print(get_disk_io())  # 磁盘IO信息
    # # main()
    # get_process()
    dns_analysis_ip('localhost')
