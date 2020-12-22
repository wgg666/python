# coding=utf-8
from 爬虫.py.headers import getheaders
from 爬虫.py.response import xy_item
import requests, parsel, time, random, threading, os, sys


# 巨人账号
def Giant_account():
    param = {
        # "account": "13265547087",
        "source": "giant_site",
        "nonce": '',
        "type": "verifycode",
        "token": '',
        "refurl": 'https://reg.ztgame.com/site/index?source=giant_site&v=normal',
        "cururl": "http://reg.ztgame.com/site/index?source=giant_site",
        "phone": "13265547087",
        "mpcode": '',
        "pwd": '',
        "tname": '',
        "idcard": ''
    }
    url = 'https://reg.ztgame.com/common/send-voice'
    headers = {
        "Cookie": "_ee70c=http://172.28.198.75:80; AM_SESSID=c4k1qb8orpq8d2n73j7pnqp7ti; ucd=4d505229901fb8499ae203ae2359818006a5a1dff0e8b30718015822b5a20ec1a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ucd%22%3Bi%3A1%3Bs%3A26%3A%22c4k1qb8orpq8d2n73j7pnqp7ti%22%3B%7D; NSC_l8t-usbfgjl-ttm-pomjof-UY-J=ffffffffaf14d61745525d5f4f58455e445a4a426d90; UM_distinctid=1760eaf9eec28f-0e90620fabc8f2-4353760-e1000-1760eaf9ef429; uniqid=2011281953144000529456; ref=0; ref_date=2020-11-28+19%3A53%3A14.0144; ref_ip=120.231.15.57; CNZZDATA1262808196=1231874534-1606559164-https%253A%252F%252Fwww.baidu.com%252F%7C1606564617; date=2020-11-28+20%3A03%3A31.1401",
        "Host": "reg.ztgame.com",
        "Referer": "https://reg.ztgame.com/site/index?source=giant_site",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br"
    }
    headers.update(getheaders(1))
    response_get = requests.get(url=url,
                                headers=headers,
                                params=param
                                )
    # xy_item(response_get)
    print('巨人账号：', response_get.text)


if __name__ == '__main__':
    Giant_account()
