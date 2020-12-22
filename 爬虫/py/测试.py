from 爬虫.py.headers import getheaders
from 爬虫.py.response import xy_item
import requests, parsel, time, random, threading, json
from queue import Queue

headers = getheaders(1)
headers.update({
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "max-age=0",
    "Cookie": "_ga=GA1.2.980476488.1602433826; channelid=0; sid=1605166836464382; _gid=GA1.2.1393743511.1605856171; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1605166635,1605712053,1605759061,1605928690; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1605936565",
    "Host": "www.kuaidaili.com",
    "Referer": "https://www.kuaidaili.com/free/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
})
print(headers)
str = 'https://www.kuaidaili.com/free/inha/1/'
print(f"https://www.kuaidaili.com/free/inha/{str.rsplit('/')[-2]}/")