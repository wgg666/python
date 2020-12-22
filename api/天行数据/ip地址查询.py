# -*- encoding: utf-8 -*-
'''
@文件    :ip地址查询.py
@说明    :
@时间    :2020/12/18 03:32:12
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
api = 'http://api.tianapi.com/txapi/ipquery/index'

headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}
data = {
    'key': 'ccac850ff60b9e3dbaa7b1be2a624242',
    "ip": '120.239.146.50'
}

response = requests.post(url=api, data=data, headers=headers)
newslist = response.json()['newslist'][0]
print({'isp':newslist['isp'],'地区编码':newslist['areacode'],'经度':newslist['longitude'],'维度':newslist['latitude'],'地址': newslist['continent']+newslist['country']+newslist['province']+newslist['city']+newslist['district']})
