import requests
#  请求头
headers = {
    # 请求载体的身份信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # 连接：保持活动
    "Connection": "keep-alive",
    "accept-language": "zh-CN,zh;q=0.9"
}
urls = [
    'https://fanyi.baidu.com/',
    'https://baidu.com/',
    'https://qq.com/'
]
def get_content(url):
    print('正在爬取:',url)
    response_get = requests.get(url=url, headers=headers)
    def xy_item(response):
        headers_list = {
            "状态码": response.status_code,
            "内容类型": response.headers["Content-Type"],
            "服务器中间件": response.headers["Server"]
        }
        print(headers_list)
    xy_item(response_get)
    if response_get.status_code == 200:
        return response_get.content

def parse_content(content):
    print('响应数据的长度为:',len(content))

for url in urls:
    content = get_content(url)
    parse_content(content)