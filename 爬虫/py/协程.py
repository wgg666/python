import asyncio
import requests,json,time

start_time = time.time()

async def request(url):
    print('正在请求的url',url)
    print('请求成功',url)
    return url
# async修饰的函数，调用之后返回的一个协程对象
c = request('www.baidu.com')

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
# # 用事件循环对象创建循环任务
# task = loop.create_task(c)
# # 
# print(task)
# 循环运行直到完成的任务
# loop.run_until_complete(task)
# print(task)

# # # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
# # 异步创建一个等待执行的任务
# task = asyncio.ensure_future(c)
# print(task)
# # 循环运行直到完成的任务
# loop.run_until_complete(task)
# print(task)

# 绑定回调
def callback_func(task):
    print(task.result())
# 创建一个事件循环对象
loop = asyncio.get_event_loop()
# 异步创建一个等待执行的任务
task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
# 运行直到完成的任务
loop.run_until_complete(task)


end_time = time.time()
print('耗时:%s秒' % (end_time - start_time))