# -*- encoding: utf-8 -*-
'''
@文件    :身份证二要素认证.py
@说明    :深圳市隆飞洋科技有限公司
@时间    :2020/12/18 00:45:42
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
api = 'https://flybigdata.market.alicloudapi.com/verify/bidverify2'

headers = {
    'Authorization': 'APPCODE 582cd5ea49744ddc98aaf2034bcb2fc0',
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}
params = {
    "certcode": '532626200108072152', #身份证
    # "mobile": '13265547087',
    "name": '李香洪' #姓名
}

response = requests.get(url=api, params=params, headers=headers)
info = response.json()
print(info)
