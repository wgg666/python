import requests
from lxml import etree
import os
if __name__ == "__main__":
    openmode = 'wb'
    url = 'http://pic.netbian.com/4kmeinv/'
        # 请求头
    headers = {
        # 请求载体的身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        # 连接：保持活动
        "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9"
    }
    response_get = requests.get(url=url, headers=headers)
    # response_get.encoding='utf-8'
    # 响应的键值对

    def xy_item(response):
        headers_list = {
            "状态码": response.status_code,
            "内容类型": response.headers["Content-Type"],
            "服务器中间件": response.headers["Server"]
        }
        print(headers_list)
    xy_item(response_get)
    page_text = response_get.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    file = '.\\爬虫\\img\\'
    if not os.path.exists(file):
        os.mkdir(file)  
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        # print(img_name,img_src)
        img_data = requests.get(url=img_src,headers=headers).content
        img_path = file + img_name
        with open(img_path,openmode,) as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')