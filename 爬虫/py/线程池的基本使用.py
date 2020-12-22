# 使用单线程串行的方式
# import time
# def get_page(str):
#     print('正在下载:',str)
#     time.sleep(2)
#     print('下载成功:',str)

# name_list = ['xiaozi','aa','bb','cc']
# start_time = time.time()
# for i in range(len(name_list)):
#     get_page(name_list[i])
# end_time = time.time()
# print('%d second' % (end_time-start_time))



import time
import datetime
import timeit
# 导入线程池模块
from multiprocessing.dummy import Pool
start_time = time.time()
def get_page(str):
    print('正在下载:'+ str + '\n')
    time.sleep(2)
    print('下载成功:',str)

name_list = ['xiaozi','aa','bb','cc']
end_time = time.time()
# 实例化一个线程池对象
pool = Pool(4)
pool.map(get_page,name_list)
print('耗时:%s秒' % (end_time - start_time))
