# coding=utf-8

import urllib.request

# 打开访问url get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# 读取并且解码
# print(response.read().decode("utf-8"))

# post请求
import urllib.parse
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
try:
    data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding="utf-8")
    # 请求对象
    req = urllib.request.Request(url = url, data = data, headers = headers, method = "POST")
    response = urllib.request.urlopen(req)
    print('状态码：' + str(response.status) + '，内容类型：' + str(response.getheader("Content-Type")) + '，服务器中间件：' + str(response.getheader("Server")))
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")
