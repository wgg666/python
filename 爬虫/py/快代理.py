from 爬虫.py.headers import getheaders
from 爬虫.py.response import xy_item
import requests, parsel, time, random, threading, json
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

# 请求
start1_time = time.time()


def get_url_list(url):
    try:
        headers = getheaders(1)
        headers.update({
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "max-age=0",
            "Cookie": "_ga=GA1.2.980476488.1602433826; channelid=0; sid=1605166836464382; _gid=GA1.2.1393743511.1605856171; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1605166635,1605712053,1605759061,1605928690; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1605936565",
            "Host": "www.kuaidaili.com",
            "Referer": f"https://www.kuaidaili.com/free/inha/{url.rsplit('/')[-2]}/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "*/*",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "X-Requested-With": "XMLHttpRequest",
            "sec-fetch-site": "cross-site",
            "x-client-data": "CJa2yQEIo7bJAQjEtskBCKmdygEIhrXKAQiZtcoBCPbHygEItMvKAQ=="
        })
        #     # 关闭警告
        requests.packages.urllib3.disable_warnings()
        # 关闭ssl认证
        response_get = requests.get(url=url, headers=headers, verify=False)
        xy_item(response_get)
        data = response_get.text
        # 解析
        # 转化成selector对象
        html_data = parsel.Selector(data)
        # 拿到所有tr标签
        parse_list = html_data.xpath('//*[@id="list"]/table/tbody/tr')
        for tr in parse_list:
            http_typt = tr.xpath('./td[4]/text()').extract_first()  # 协议类型
            ip_num = tr.xpath('./td[1]/text()').extract_first()  # IP地址
            ip_port = tr.xpath('./td[2]/text()').extract_first()  # 端口
            # print(http_typt,ip_num,ip_port)
            # ip池字典
            proxies_dict = {}
            proxies_dict["http"] = 'http://' + ip_num + ':' + ip_port
            proxies_dict["https"] = 'http://' + ip_num + ':' + ip_port
            proxies_list.append(proxies_dict)
    except requests.exceptions.ConnectionError:
        print('连接错误：超过了最大重试次数,访问频繁？被ban IP？')
    except requests.exceptions.ProxyError:
        print('代理错误：由于目标计算机积极拒绝无法连接,值只能是http协议')
    except requests.exceptions.ConnectTimeout:
        print('连接超时')
    except requests.exceptions.InvalidURL:
        print('无效的URL：端口错误')
    except AttributeError:
        print('属性错误：proxies参数应传入字典而不是字符串')
    finally:
        # print('当前线程：', threading.current_thread(), '\n')
        print(f'爬取了{len(url_lists)}页,IP数量：{len(proxies_list)}')


# 检测IP可用性# 检测IP可用性
start2_time = time.time()


def check_ip(proxy):
    url = 'https://www.baidu.com'
    try:
        response_get = requests.get(url=url, headers=getheaders(1), proxies=proxy, timeout=2, stream=True, verify=False)
        xy_item(response_get)
        if response_get.status_code == 200:
            can_use.append(proxy)
    except requests.exceptions.ProxyError:
        print('代理错误：由于目标计算机积极拒绝无法连接,值只能是http协议')
    except requests.exceptions.ConnectTimeout:
        print('连接超时')
    except requests.exceptions.ReadTimeout:
        print('读取超时：HTTP连接池读取超时')
    except requests.exceptions.ChunkedEncodingError:
        print('分块编码错误：连接断开：连接重置错误,解决：下载大文件设置 stream=True')
    except requests.exceptions.InvalidURL:
        print('无效的URL：端口错误')
    except AttributeError:
        print('属性错误：proxies参数应传入字典而不是字符串')
    finally:
        print('当前线程：', threading.current_thread(), '\n')


# 线程池
def Create_thread_pool(num, fun, list, sleep):
    # 1.创建线程池
    pool = ThreadPoolExecutor(max_workers=num)
    # # 2.指定对应任务和参数
    # [pool.submit(fun, i) for i in list]
    for i in list:
        pool.submit(fun, i)
        # 随机等待
        time.sleep(sleep)
    # 3.关闭线程池
    pool.shutdown()


if __name__ == '__main__':
    # with open('.\\爬虫\\py\\proxies_list.json','a+') as proxies_list:
    #     json.dump
    # ip池列表
    proxies_list = []
    proxies_list.append({"http": "http://192.168.100.3:8888", "https": "http://192.168.100.3:8888"})
    # 所有高匿ip页面
    url_lists = [f'https://www.kuaidaili.com/free/inha/{pageNum}/' for pageNum in range(1, 10)]
    # 爬IP线程池
    Create_thread_pool(15, get_url_list, url_lists, 1.1)
    end1_time = time.time()
    print(f'爬取IP耗时{end1_time - start1_time}秒')
    # print(proxies_list)
    # 清洗出的IP
    can_use = []
    # 请求的url列表

    ## 清洗ip线程池
    Create_thread_pool(20, check_ip, proxies_list, 0.01)
    end2_time = time.time()
    print(f'可用IP池：{can_use}\n可用IP数量：{len(can_use)}')
    print(f'清洗IP耗时{end2_time - start2_time}秒')
