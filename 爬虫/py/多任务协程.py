import asyncio,time,os,requests,aiohttp

start_time = time.time()
headers = {
    # 请求载体的身份信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # 连接：保持活动
    "Connection": "keep-alive",
    "accept-language": "zh-CN,zh;q=0.9"
}
urls = [
    'https://www.baidu.com',
    'https://www.qq.com',
    'https://www.hao123.com'
]
async def get_page(url):
    print('正在下载',url)
    async with aiohttp.ClientSession() as session:
        # get()、post()
        #headers(设置请求头)、params(get传参)、data(post传参)
       async with await session.get(url,headers=headers) as response_get:
        #    获取响应数据操作之前一定要使用await进行手动挂起
        page_text = await response_get.text()
        def xy_item(response):
            headers_list = {
                "状态码": response.status,
                "内容类型": response.headers["Content-Type"],
                "服务器中间件": response.headers["Server"]
            }
            print(headers_list)
        xy_item(response_get)

    print('下载完毕：',url)


# # 任务列表
stasks = []
for url in urls:
    c = get_page(url)
    # 任务对象
    task = asyncio.ensure_future(c)
    stasks.append(task)
    # 循环对象
    loop = asyncio.get_event_loop()
    # 循环运行直到完成异步等待状态的任务
    loop.run_until_complete(asyncio.wait(stasks))
    # print(task)
end_time = time.time()
print('耗时:%s秒' % (end_time - start_time))