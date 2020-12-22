# coding=utf-8
from tkinter import *
from socket import *


class Ps_server:
    def __init__(self):
        self.ip_str = StringVar().set('192.168.100.3')
        self.port_str = StringVar().set('8000')
        self.get_info_str = StringVar().set('cpu')
        self.ip = None
        self.port = None
        self.data = None
        self.c_sock = socket(AF_INET, SOCK_STREAM)
        self.root = Tk()
        self.root.geometry('300x300+250+250')

        self.et_ip = Entry(self.root, width=30, textvariable=self.ip_str)
        self.et_port = Entry(self.root, width=6, textvariable=self.port_str)
        self.et_get_info = Entry(self.root, width=5, textvariable=self.get_info_str)

        self.ip_label = Label(self.root, text='IP地址', width=10)
        self.port_label = Label(self.root, text='端口', width=10)
        self.la_data = Label(self.root, text='信息...')

        self.bt_conn = Button(self.root, text='连接', width=5, height=1,
                              command=self.connect)
        self.bt_close = Button(self.root, text='断开', width=5, height=1,
                               state='disable', command=self.close)
        self.bt_get_info = Button(self.root, text='获取', width=5, height=1,
                                  state='disable', command=self.get_server_info)




    def main(self):
        self.et_ip.place(x=0, y=0)
        self.ip_label.place(x=150, y=0)

        self.et_port.place(x=0, y=30)
        self.port_label.place(x=50, y=30)

        self.bt_conn.place(x=0, y=60)
        self.bt_close.place(x=100, y=60)
        self.et_get_info.place(x=0, y=100)
        self.bt_get_info.place(x=200, y=100)

        self.la_data.place(x=0, y=130)
        self.root.mainloop()

    def connect(self):
        self.ip = self.et_ip.get()
        self.port = self.et_port.get()
        print(f'{self.ip}:{self.port}')

        self.la_data['text'] = '正在连接'
        try:
            self.c_sock.connect((str(self.ip), int(self.port)))
        except Exception as e:
            print(e)
            self.la_data['text'] = '连接失败'
        else:
            self.bt_close['state'] = 'normal'
            self.bt_get_info['state'] = 'normal'
            self.la_data['text'] = '连接成功'

    def close(self):
        self.c_sock.close()
        self.bt_close['state'] = 'disable'
        self.bt_get_info['state'] = 'disable'
        self.la_data['text'] = '连接断开...'

    def get_server_info(self):
        buf = self.et_get_info.get()
        self.c_sock.send(buf.encode('utf-8'))
        data = self.c_sock.recv(1024).decode('utf-8')
        if not data:
            self.la_data['text'] = '远程主机断开...'
        self.la_data['text'] = data


if __name__ == '__main__':
    ps = Ps_server()
    ps.main()
