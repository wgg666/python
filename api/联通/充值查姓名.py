# -*- encoding: utf-8 -*-
'''
@文件    :充值查姓名.py
@说明    :
@时间    :2020/12/18 13:38:46
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
import sys
from api.联通.MallLogin import session

api = 'https://upay.10010.com/npfweb/NpfWeb/customInfo/cellInfoQuery'

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://upay.10010.com/npfweb/npfcellweb/phone_recharge_fill.htm",
    "sec-ch-ua": 'Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}
# print(session.headers)
params = {
    "commonBean.phoneNo": input('手机号：'), #查询的手机号
    "loginPhoneNo": "13265547087" #本人手机号
}

response = session.get(url=api, params=params, headers=headers)
# print(session.cookies.get_dict()) #cookie字典
# print(session.headers)
info = response.json()
if info['isLogin'] == False:
    print('cookie失效！！！')
else:
    print(info)
