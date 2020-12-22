import requests
from lxml import etree
import os
codemode = 'wb'
filemode = 'w'
file = '.\\爬虫\\html\\gushiwen.html'
code = '.\\爬虫\\code\\code.jpg'
host = 'https://so.gushiwen.cn'
url = 'https://so.gushiwen.cn/user/login.aspx'
# 请求头
headers = {
    # 请求载体的身份信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # 连接：保持活动
    "Connection": "keep-alive",
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

page_text = response_get.text
tree = etree.HTML(page_text)
code_img_src = host + tree.xpath('//*[@id="imgCode"]/@src')[0]
# 请求验证码地址得到二进制图片数据
img_data = requests.get(url=code_img_src,headers=headers).content
with open(code,codemode) as fp:
    fp.write(img_data)
    print('验证码下载成功！！！')
# 得到验证码
def getCodeText(imgPath):
    filename = imgPath
    # 打开图片
    os.startfile(filename)
getCodeText(code)
# 存储验证码
code_text = input('请输入验证码：')
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
data = {
    '__VIEWSTATE':'qsgArVzwHEX9s/u2+I0HjWJ4DyXJS3GkSKqJ5NRVNNe8jek+NSi5xdxzB/iyWmZqoUc7KZRhWuhQXSzX9rh0xLAvu37yWKWtQzXM7mC3gydtTLxk0dA/oQ2Qkrg=',
    '__VIEWSTATEGENERATOR':'C93BE1AE',
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'2861104332@qq.com',
    'pwd':'XWL520886',
    'code':code_text,
    'denglu':'登录'
}
headers = {
    # 请求载体的身份信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # 连接：保持活动
    "Connection": "keep-alive",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "login=flase; ASP.NET_SessionId=udo2m0wvkn1vgyi4dt40i2hx; Hm_lvt_9007fab6814e892d3020a64454da5a55=1605155393; login=flase; gswZhanghao=2861104332%40qq.com; wsEmail=2861104332%40qq.com; codeyzgswso=bacac34718d2d1d5; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1605161145",
    "origin": "https://so.gushiwen.cn",
    "referer": "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx",
}

response_post = requests.post(url=login_url,headers=headers,data=data)
xy_item(response_post)
login_page_text = response_post.text
with open(file,filemode,encoding='utf-8') as fp:
    fp.write(login_page_text)
