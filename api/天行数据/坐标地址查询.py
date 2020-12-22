# -*- encoding: utf-8 -*-
'''
@文件    :坐标地址查询.py
@说明    :
@时间    :2020/12/18 03:17:16
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
api = 'http://api.tianapi.com/txapi/geoconvert/index'

headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}
data = {
    'key': 'ccac850ff60b9e3dbaa7b1be2a624242',
    'lng': '110.286209', #经度
    "lat": '21.609700' #维度
}

response = requests.post(url=api, data=data, headers=headers)
newslist = response.json()['newslist'][0]
print({'城镇编码':newslist['town_code'],'身份证编码':newslist['adcode'],'地址':newslist['country'] + newslist['province'] + newslist['city'] + newslist['district'] + newslist['street'] + newslist['town'] + newslist['street_number']})
