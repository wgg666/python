import requests
import os
import json

if __name__ == "__main__":
    writemode = 'wb'
    # 请求关键词参数
    # kw = input('关键词：')
    param = {
        # 'query':
        # "type": '24',
        # "interval_id": '100:90',
        # "action": '',
        # "start": '0',
        # "limit": '20'
    }
    url = 'https://pic.qiushibaike.com/system/pictures/12377/123776201/medium/I7WBBWVXUEUZ02QO.jpg'
    
    # 获取当前文件所在目录
    filename = f'{os.path.dirname(__file__)}\\img\\qiutu.jpg'
    # jsonname = f'{os.path.dirname(__file__)}\\shuju\\douban.json'
    # 请求头
    headers = {
        #请求载体的身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        #连接：保持活动
        "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9"
    }

    # 发起get请求
    response_get = requests.get(url=url,params=param,headers=headers)
    # 响应的键值对
    def xy_item(response):
        headers_list = {
            "状态码":response.status_code,
            "内容类型":response.headers["Content-Type"],
            "服务器中间件":response.headers["Server"]
            }
        for item in headers_list:
            print(item,headers_list[item],sep='：')
    xy_item(response_get)
    img_data = response_get.content
    with open(filename,writemode) as fp:
        fp.write(img_data)