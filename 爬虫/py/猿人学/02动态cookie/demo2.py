# -*- encoding: utf-8 -*-
'''
@文件    :1.py
@说明    :
@时间    :2020/12/15 22:57:21
@作者    :AwAit
@版本    :1.0
'''

from 爬虫.py.headers import getheaders
from 爬虫.py.response import xy_item
import requests
import parsel
import time
import random
import threading
import json
import execjs
import urllib.parse


with open(r'.\爬虫\py\猿人学\02动态cookie\2.js', encoding='utf-8') as f:
    JsData = f.read()

cookie = execjs.compile(JsData).call('$_0x5801ee')
jiage_list = []
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "cookie": 'm={}'.format(cookie),
    "Host": "match.yuanrenxue.com",
    "Referer": "http://match.yuanrenxue.com/match/2",
    "User-Agent": "yuanrenxue.project",
    "X-Requested-With": "XMLHttpRequest",
}

for i in range(1, 6):
    url = 'http://match.yuanrenxue.com/api/match/2?page=%s' % i
    # 关闭ssl认证
    response_get = requests.get(url=url, headers=headers)
    xy_item(response_get)
    data = response_get.json()
    print(data)
    for i in range(len(data['data'])):
        jiage_list.append(data['data'][i]['value'])
print(jiage_list)
print({'总和': sum(jiage_list),'平均价格':sum(jiage_list) / len(jiage_list), '数量':len(jiage_list)})
