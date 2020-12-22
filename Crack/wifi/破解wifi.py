import pywifi
from pywifi import const

# 判断是否有无线网卡连接
def gic():
    # 创建wifi对象
    wifi = pywifi.PyWiFi()
    # print(wifi)
    # 无线网卡
    ifaces = wifi.interfaces()
    return wifi,ifaces

def get_wk_info():
    ifaces = gic()[1]
    # 所有无线网卡名字和状态
    wireless_network_adapter = {}
    for ifaces in ifaces:
        # 如果断开连接
        if ifaces.status() == const.IFACE_DISCONNECTED:
            ifaces_status = '未连接'
        else:
            ifaces_status = '已连接'
        wireless_network_adapter[str(ifaces.name())] = ifaces_status        

    return wireless_network_adapter

def get_wk_name(name_key):
    wireless_network_adapter = get_wk_info()
    # 所有网卡名字
    wireless_network_adapter_name = []
    for key in wireless_network_adapter.keys():
        wireless_network_adapter_name.append(key)
    return wireless_network_adapter_name[name_key]

# 扫描附近wifi
def bies():
    # 选择网卡
    ifaces = gic()[0].interfaces()[1]
    # 扫描wifi
    ifaces.scan()
    # 获取扫描之后的结果
    res = ifaces.scan_results()
    # print(res)
    for data in res:
        print(data.ssid)

# 程序入口
if __name__ == '__main__':
    gic()
    # 网卡键值对
    print(get_wk_info())
    # 第1张网卡
    print(get_wk_name(1))
    # 输出附近wifi
    bies()
    # MERCURY_83BA
    # TP-LINK_B213