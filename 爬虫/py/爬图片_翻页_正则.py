import requests
import os
import json
import re

if __name__ == "__main__":
    imgdir = '.\\爬虫\\qiutuLibs\\'
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists(imgdir):
        os.mkdir(imgdir)
    writemode = 'wb'
    # 单页
    url = 'https://www.qiushibaike.com/imgrank/'
    # 设置一个通用的url模板
    urls = 'https://www.qiushibaike.com/imgrank/page/%d/'
    # 遍历所有下一页
    for pageNum in range(1,14):
        #对应页码的url
        new_url = format(urls%pageNum)
        # 请求头
        headers = {
            #请求载体的身份信息
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            #连接：保持活动
            # "Connection": "keep-alive",
            # "accept-language": "zh-CN,zh;q=0.9"
        }

        # 发起get请求
        response_get = requests.get(url=new_url,headers=headers)
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
        # html页面
        page_text = response_get.text
        # 正则表达式
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        # 图片地址列表
        img_src_list = re.findall(ex,page_text,re.S)
        # print(img_src_list)
        #遍历一页的所有图片地址
        for src in img_src_list:
            src = 'https:' + src
            response_get = requests.get(url=src,headers=headers)
            img_data = response_get.content
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片存储路径
            imgPath = imgdir + img_name
            # 保存图片
            with open(imgPath,writemode) as fp:
                fp.write(img_data)
                print(img_name,'下载成功！！！')