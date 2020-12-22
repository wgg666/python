# coding=utf-8
import os
import sys
import threading
import time

from pynput import keyboard  # 键盘库
from pynput.keyboard import Controller, Key, Listener


# 每隔秒清空列表
def doWaiting():
    while True:
        time.sleep(10)
        all_key.clear()


# 键盘按压
def on_press(key):
    pass


def start_listen():
    with Listener(on_press=None, on_release=on_release) as listener:
        listener.join()


# 键盘松开
def on_release(key):
    all_key.append(str(key))
    print(all_key)

    if 'key.ctrl_l' in all_key and 'c' in all_key:
        print('复制快捷键')
    if 'key.ctrl_l' in all_key and 'v' in all_key:
        print('粘贴快捷键')

    if key == Key.esc:
        # 停止监听
        return False


if __name__ == '__main__':
    all_key = []
    t = threading.Thread(target=doWaiting)
    t.setDaemon(True)  # 守护进程
    t.start()
    start_listen()
