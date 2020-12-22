# -*- encoding: utf-8 -*-
'''
@文件    :查余额.py
@说明    :
@时间    :2020/12/18 13:54:35
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
from api.联通.MallLogin import session

api = 'https://iservice.10010.com/e3/static/query/userinfoE5query'
"""
#  piw=%7B%22login_name%22%3A%22132****7087%22%2C%22nickName%22%3A%22%E5%A4%8F%E4%BC%9F%E9%9C%96%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2213265547087%22%7D%2C%22verifyState%22%3A%22%22%7D;
#   _uop_id=d4c9553c3071e3c9be4711c72ea75cf6; 
#   JUT=vnFkeilnirUlhh1r4mm4+TCv6nT2P6dYRp/75L+m+2UVnvosjLTnaW4sF+ypYO8f5dXSmeT4TbG5FD3HsYBpNOSZ2V5evSxu5tQ86AxNZH9IPFFQRiFJKmuKkwS/GRMHwlNC/kvjMQb/uEWsj21xVuXsmsCOWY8fbvzz9G/jO/fl3btXglVBAr9G7Ik39R/UwJwltTVhstfjn26e+roQyKOcRXYIyyURKNIK6/OJgZ+52CMNb/lTm07qACdrii8ftAAzC3VO9qd0BsuS55K1Nq2H8Yr/9VaeqJpKOaTbZZkt7h404GSRKCE4uKlpJwzmFDrOul3pLjJp1f6VdpkbFMIsjcRrxVXjMyWnZhcSPW8/aS5JY3jD2WE3k1qagSkflZeA4V1ddf9DyWx/AEj8EhvKlvIQJBrD/5LhIYjG6MgPpjGaeGRzRpIo5Jae9c3IMtF6vnCjzJs65KpKKvLTMLHxi3bIzitYAr+9tnRnq+jwqnnAL+rsbhJdkd0S6+8lTB5WLSpj2Bk=QJyjFXnZRDbw/bSAWUikXA==
"""
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    # "cookie": "JSESSIONID=2D9FF0F2B915F995402ECF298061F29D; route=16a87357b753cde2d25151a8073ec4b3; SHOP_PROV_CITY=; CaptchaCode=zLuK3veOwaLuBKjiMD7ub+ZWW5v2MhD16TSJ0MJ9h9s=; UID=uOKPrHvzb6avS14BGuteqtMEQnqPUdEo; WT_FPC=id=268ee0b80caeef2239a1608269361805:lv=1608269382083:ss=1608269361805; cien=; userprocode=051; WT=13265547087; guide=true; upay_user=270ca16d177e069c5c014f3f7203e13a; piw=%7B%22login_name%22%3A%22132****7087%22%2C%22nickName%22%3A%22%E5%A4%8F%E4%BC%9F%E9%9C%96%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2213265547087%22%7D%2C%22verifyState%22%3A%22%22%7D; _uop_id=d4c9553c3071e3c9be4711c72ea75cf6; citycode=540; mallflag=null; loginflag=true; _pk_ref.4.7bb6=%5B%22%22%2C%22%22%2C1608289730%2C%22https%3A%2F%2Fupay.10010.com%2F%22%5D; _pk_ses.4.7bb6=1; mallcity=51|510; _pk_id.4.7bb6=9b8fbf46993c0623.1608269609.3.1608289837.1608289730.; JUT=vnFkeilnirUlhh1r4mm4+TCv6nT2P6dYRp/75L+m+2UVnvosjLTnaW4sF+ypYO8f5dXSmeT4TbG5FD3HsYBpNOSZ2V5evSxu5tQ86AxNZH9IPFFQRiFJKmuKkwS/GRMHwlNC/kvjMQb/uEWsj21xVuXsmsCOWY8fbvzz9G/jO/fl3btXglVBAr9G7Ik39R/UwJwltTVhstfjn26e+roQyKOcRXYIyyURKNIK6/OJgZ+52CMNb/lTm07qACdrii8ftAAzC3VO9qd0BsuS55K1Nq2H8Yr/9VaeqJpKOaTbZZkt7h404GSRKCE4uKlpJwzmFDrOul3pLjJp1f6VdpkbFMIsjcRrxVXjMyWnZhcSPW8/aS5JY3jD2WE3k1qagSkflZeA4V1ddf9DyWx/AEj8EhvKlvIQJBrD/5LhIYjG6MgPpjGaeGRzRpIo5Jae9c3IMtF6vnCjzJs65KpKKvLTMLHxi3bIzitYAr+9tnRnq+jwqnnAL+rsbhJdkd0S6+8lTB5WLSpj2Bk=QJyjFXnZRDbw/bSAWUikXA==",
    "cookie": 'JSESSIONID=2D9FF0F2B915F995402ECF298061F29D; route=16a87357b753cde2d25151a8073ec4b3; SHOP_PROV_CITY=; CaptchaCode=zLuK3veOwaLuBKjiMD7ub+ZWW5v2MhD16TSJ0MJ9h9s=; UID=uOKPrHvzb6avS14BGuteqtMEQnqPUdEo; WT_FPC=id=268ee0b80caeef2239a1608269361805:lv=1608269382083:ss=1608269361805; cien=; userprocode=051; WT=13265547087; guide=true; upay_user=270ca16d177e069c5c014f3f7203e13a; citycode=540; mallflag=null; loginflag=true; _pk_ref.4.7bb6=%5B%22%22%2C%22%22%2C1608289730%2C%22https%3A%2F%2Fupay.10010.com%2F%22%5D; _pk_ses.4.7bb6=1; mallcity=51|510; _pk_id.4.7bb6=9b8fbf46993c0623.1608269609.3.1608289837.1608289730.;',
    "origin": "https://iservice.10010.com",
    "pragma": "no-cache",
    "referer": "https://iservice.10010.com/e5/query.html",
    "sec-ch-ua": 'Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}
params = {
    '_': '%s' % int(time.time() * 1000)
}

response = session.post(url=api, params=params, headers=headers)
try:
    info = response.json()
    resource = info['resource']
    userInfo = info['userInfo']
    print({'可用余额': resource['balance'],'实时话费': resource['realFee'],
    '剩余流量':resource['remainFlow'], '已用流量': resource['usedFlow']})
except:
    print('cookie失效！！！')