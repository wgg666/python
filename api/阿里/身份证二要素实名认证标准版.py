# -*- encoding: utf-8 -*-
'''
@文件    :身份证二要素实名认证标准版.py
@说明    :深圳云码通科技有限公司
@时间    :2020/12/18 00:49:14
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
from uuid import uuid4
api = 'https://pidysc2zx.market.alicloudapi.com/pidinfo/ysc2zx'

headers = {
    'Authorization': 'APPCODE 582cd5ea49744ddc98aaf2034bcb2fc0',
    'X-Ca-Nonce': str(uuid4()), #'ec0695a4-4fa3-452b-a7b0-9a76119bf190'
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}
data = {
    "idcard": '532626200108072152', #身份证
    # "mobile": '13265547087',
    "realname": '李香洪' #姓名
}

response = requests.post(url=api, data=data, headers=headers)
info = response.json()
print(info['result'])
# print(info)
