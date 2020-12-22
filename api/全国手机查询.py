# -*- encoding: utf-8 -*-
'''
@文件    :全国手机查询.py
@说明    :
@时间    :2020/12/18 01:46:11
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
import parsel
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=POl_98XZ9Pgfd0ZmGPXHqVjTjzlkj3YNRadYtaZcENR9p9NIcMsdelXtqpE7K0gKGhjyvNGlXjkaXuZpAA-3Qa&wd=&eqid=d7dfa3d60018e89b000000065fdb97f3; UM_distinctid=17671c9c507476-06541103506917-c791039-e1000-17671c9c508325; CNZZDATA1253279987=1808620482-1608226816-https%253A%252F%252Fwww.baidu.com%252F%7C1608226816",
    "Host": "www.tiantianxieye.com",
    "Referer": "http://www.tiantianxieye.com/nub/search.php",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}

response = requests.get(url='http://www.tiantianxieye.com/nub/%s.html' % input('手机号：'), 
    headers=headers
)
response.encoding='gb2312'
phoneinfo = response.text
html_data = parsel.Selector(phoneinfo)
# # 拿到所有div标签
parse_list = html_data.xpath('//*[@class="mU"]')
# print(parse_list.get('data'))
sjh = parse_list.xpath('./div[2]/span[2]/text()').extract_first()  # 手机号
gsd = parse_list.xpath('./div[3]/span[2]/text()').extract_first()  # 归属地
quhao = parse_list.xpath('./div[4]/span[2]/text()').extract_first() #区号
katype = parse_list.xpath('./div[5]/span[2]/text()').extract_first() #卡号类型
print({'手机号':sjh, '卡号归属地':gsd, '归属地区号':quhao, '卡号类型':katype})
