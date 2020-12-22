from pynput.mouse import Button, Controller as mouse_cl
from pynput.keyboard import Key, Controller as key_cl
import time


def send_message(str):
    for i in range(10):
        mouse = mouse_cl()  # 鼠标权限定位
        mouse.press(Button.left)  # 点击左键
        mouse.release(Button.left)  # 松开左键
        keyboard = key_cl()  # 键盘管理员权限
        keyboard.type(str)

        keyboard.press(Key.enter)  # 回车
        keyboard.release(Key.enter)  # 松开回车
        time.sleep(1)


if __name__ == '__main__':
    send_message('你妈隔壁')
