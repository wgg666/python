from lxml import etree
import requests

url = 'https://so.gushiwen.cn/user/collect.aspx'
# 创建一个session对象
session = requests.Session()
headers = {
    # 请求载体的身份信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # 连接：保持活动
    "Connection": "keep-alive",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1605155393; wsEmail=2861104332%40qq.com; codeyzgswso=b67f846fb9a21af2; gsw2017user=1396391%7cF1219F80F7DFEDE59E8FD5EB8B7C9818; login=flase; wxopenid=defoaltid; gswZhanghao=2861104332%40qq.com; gswEmail=2861104332%40qq.com; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1605164280"
}
response_get = session.get(url=url, headers=headers)
# 响应的键值对

def xy_item(response):
    headers_list = {
        "状态码": response.status_code,
        "内容类型": response.headers["Content-Type"],
        "服务器中间件": response.headers["Server"]
    }
    print(headers_list)
xy_item(response_get)

print(response_get.text)