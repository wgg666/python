# -*- encoding: utf-8 -*-
'''
@文件    :身份证查询.py
@说明    :
@时间    :2020/12/18 02:48:24
@作者    :AwAit
@版本    :1.0
'''


import requests
import time
api = 'http://api.tianapi.com/txapi/sfz/index'

headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}
data = {
    'key': 'ccac850ff60b9e3dbaa7b1be2a624242',
    'idcard': '440881199112290330'
}

response = requests.post(url=api, data=data, headers=headers)
text = response.json()
if text['msg'] == '数据返回为空':
    print('身份证无效！！！')
else: 
    print(text['newslist'][0])

