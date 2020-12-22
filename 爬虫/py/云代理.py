from 爬虫.py.headers import getheaders
from 爬虫.py.response import xy_item
import requests, parsel, time, random, threading, os, sys
from concurrent.futures import ThreadPoolExecutor


# 继承object类
class Ip3366(object):
    def __init__(self):
        self.headers = getheaders(1)
        # ip池列表
        self.proxies_list = [{"http": "http://192.168.100.3:8888", "https": "http://192.168.100.3:8888"}]
        # 清洗出的IP
        self.can_use = []
        # 请求的url列表
        self.base_urls = [f'http://www.ip3366.net/free/?stype=1&page={pageNum}' for pageNum in range(1, 8)]

    # 请求
    start1_time = time.time()

    # 发起请求
    def request(self, url, **arg):
        return requests.get(url=url, headers=self.headers, proxies=arg['proxies'], verify=False, timeout=arg['timeout'])

    # 获取IP
    def get_ip(self, url):
        response_get = self.request(url, proxies={}, timeout=120)
        xy_item(response_get)
        response_get.encoding = 'gbk'
        data = response_get.text

        # 解析
        # 转化成selector对象
        html_data = parsel.Selector(data)
        # 拿到所有tr标签
        parse_list = html_data.xpath('//*[@id="list"]/table/tbody/tr')
        for tr in parse_list:
            http_typt = tr.xpath('./td[4]/text()').extract_first().lower()  # 协议类型
            ip_num = tr.xpath('./td[1]/text()').extract_first()  # IP地址
            ip_port = tr.xpath('./td[2]/text()').extract_first()  # 端口
            # print(http_typt,ip_num,ip_port)
            # ip池字典
            proxies_dict = {}
            proxies_dict["http"] = 'http://' + ip_num + ':' + ip_port
            proxies_dict["https"] = 'http://' + ip_num + ':' + ip_port
            self.proxies_list.append(proxies_dict)
        sys.stdout.write(f'爬取了{len(self.base_urls)}页,IP数量：{len(self.proxies_list)}\n')
        # 随机等待
        time.sleep(random.random() * 3)

    # 检测IP可用性
    start2_time = time.time()

    # 清洗ip
    def check_ip(self, ip):
        sys.stdout.write('================================================正在检测IP质量================================================\n')
        try:
            response_get = self.request('https://www.baidu.com', proxies=ip, timeout=1)
            # print(ip)
            # 随机等待
            time.sleep(random.random() * 3)
            xy_item(response_get)
            if response_get.status_code == 200:
                self.can_use.append(ip)
        except requests.exceptions.ProxyError:
            sys.stdout.write('代理错误：由于目标计算机积极拒绝无法连接,值只能是http协议\n')
        except requests.exceptions.ConnectTimeout:
            sys.stdout.write('连接超时\n')
        except requests.exceptions.InvalidURL:
            sys.stdout.write('无效的URL：端口错误\n')
        except AttributeError:
            sys.stdout.write('属性错误：proxies参数应传入字典而不是字符串\n')

    # 线程池
    def Create_thread_pool(self, num, fun, list):
        # 1.创建线程池
        pool = ThreadPoolExecutor(max_workers=num)
        # 2.指定对应任务和参数
        # [pool.submit(fun, i) for i in list]
        for i in list:
            pool.submit(fun, i)
        # 3.关闭线程池
        pool.shutdown()


if __name__ == '__main__':
    ip3366 = Ip3366()
    # 爬IP线程池
    ip3366.Create_thread_pool(8, ip3366.get_ip, ip3366.base_urls)
    end1_time = time.time()
    print(ip3366.proxies_list)
    sys.stdout.write(f'爬取IP耗时{end1_time - ip3366.start1_time}秒\n')

    # 清洗ip线程池
    ip3366.Create_thread_pool(10, ip3366.check_ip, ip3366.proxies_list)
    end2_time = time.time()
    sys.stdout.write(f'可用IP池：{ip3366.can_use}\n可用IP数量：{len(ip3366.can_use)}\n')
    sys.stdout.write(f'清洗IP耗时{end2_time - ip3366.start2_time}秒\n')
