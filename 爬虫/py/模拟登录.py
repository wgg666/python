import requests
from lxml import etree
import os
openmode = 'wb'
code = '.\\爬虫\\code\\code.jpg' 
host = 'https://so.gushiwen.cn'
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
# 请求头
headers = {
    # 请求载体的身份信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # 连接：保持活动
    "Connection": "keep-alive",
    "accept-language": "zh-CN,zh;q=0.9"
}
response_get = requests.get(url=url, headers=headers)
# 响应的键值对

def xy_item(response):
    headers_list = {
        "状态码": response.status_code,
        "内容类型": response.headers["Content-Type"],
        "服务器中间件": response.headers["Server"]
    }
    print(headers_list)
xy_item(response_get)
