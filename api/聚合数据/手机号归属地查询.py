# -*- encoding: utf-8 -*-
'''
@文件    :手机号归属地查询.py
@说明    :
@时间    :2020/12/18 01:17:51
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
api = 'http://apis.juhe.cn/mobile/get'

headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}
params = {
    'phone': 13265547087,
    "dtype": 'json',
    'key': 'faaf7a011673af23472c3e9a5603e6bc'
}

response = requests.get(url=api, params=params, headers=headers)
phoneinfo = response.json()
print(phoneinfo['result'])