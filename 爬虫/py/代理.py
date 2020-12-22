from lxml import etree
import requests
import os

#
# 访问 http://icanhazip.com/（https://icanhazip.com/） 可以得到你访问时的ip地址
url = 'http://dev.kdlapi.com/testproxy'
proxies = {'http': 'http://49.70.33.154:9999', 'https': 'http://49.70.33.154:9999'}
# proxies = {'HTTP': 'HTTP://192.168.100.3:8888','HTTPS': 'HTTPS://192.168.100.3:8888'}
# 请求头
headers = {
    # 请求载体的身份信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # 连接：保持活动
    # "Connection": "keep-alive",
    "accept-language": "zh-CN,zh;q=0.9"
}
try:
    response_get = requests.get(url=url, headers=headers, proxies=proxies, verify=False, timeout=3)
    delay = response_get.elapsed.total_seconds()
    print(f'当前代理ip：{proxies}检测通过,延迟：{delay}')


    # 响应的键值对

    def xy_item(response):
        headers_list = {
            "状态码": response.status_code,
            "内容类型": response.headers["Content-Type"],
            "服务器中间件": response.headers["Server"]
        }
        print(headers_list)


    xy_item(response_get)
    # response_get.encoding = 'gbk'
    print(response_get.text)
except requests.exceptions.ProxyError:
    print('代理错误：由于目标计算机积极拒绝无法连接,值只能是http协议')
except requests.exceptions.ConnectTimeout:
    print('连接超时')
except requests.exceptions.InvalidURL:
    print('无效的URL：端口错误')
except AttributeError:
    print('属性错误：proxies参数应传入字典而不是字符串')

# 判断代理是否有效的方法
# import telnetlib
# try:
# 	telnetlib.Telnet('119.147.210.236', port='3128', timeout=3)
# except:
# 	print('ip无效！')
# else:
# 	print('ip有效！')
