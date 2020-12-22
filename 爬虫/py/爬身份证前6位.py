# -*- encoding: utf-8 -*-
'''
@文件    :爬身份证前6位.py
@说明    :
@时间    :2020/12/18 22:07:44
@作者    :AwAit
@版本    :1.0
'''
from 爬虫.py.headers import getheaders
from 爬虫.py.response import xy_item
import requests, parsel, time, random, threading, json
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

url = 'https://blog.csdn.net/monkeybananas/article/details/89671786'
headers = getheaders(1)
#     # 关闭警告
requests.packages.urllib3.disable_warnings()
# 关闭ssl认证
response_get = requests.get(url=url, headers=headers, verify=False)
xy_item(response_get)
data = response_get.text
# 解析
# 转化成selector对象
html_data = parsel.Selector(data)
print(html_data)
# parse_list = html_data.xpath('//*[@id="cnblogs_post_body"]')
# print(parse_list)
