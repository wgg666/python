# -*- encoding: utf-8 -*-
'''
@文件    :查询姓名.py
@说明    :
@时间    :2020/12/17 20:31:08
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
import json
import demjson
import ast
import yaml
api = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=%s' % input(
    '手机号：')

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "v=0; cookie2=1e90570c2c0c95fdb7cf72c76a1ab14c; t=b59fd006f6d3f65ee96411618fe7e80c; _tb_token_=ea8eeb5b3e577",
    "sec-ch-ua": 'Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}

response = requests.get(url=api, headers=headers)
phoneinfo_replace = response.text\
    .replace('__GetZoneResult_ = ', '')\
    .replace('mts','"mts"')\
    .replace('province','"province"')\
    .replace('catName','"catName"')\
    .replace('telString','"telString"')\
    .replace('areaVid','"areaVid"')\
    .replace('ispVid','"ispVid"')\
    .replace('carrier','"carrier"')
phoneinfo = ast.literal_eval(phoneinfo_replace)
print({"telString": phoneinfo['telString'],"carrier": phoneinfo['carrier']})