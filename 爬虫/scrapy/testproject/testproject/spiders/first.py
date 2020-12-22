import scrapy
from 爬虫.py.response import xy_item
from 爬虫.scrapy.testproject.testproject.items import TestprojectItem
class FirstSpider(scrapy.Spider):
    name = 'first' #爬虫文件名称
    # 允许的域名:限定start urls列表中哪些url可以进行请求发送
    # allowed_domains = ['www.xxx.com']
    # 起始的url列表
    # 'http://www.qiushibaike.com/text/'
    start_urls = ['http://www.qiushibaike.com/text/']

    # 数据解析：response参数表示的就是请求成功的响应对象
    def parse(self, response):
        xy_item(response)
        div_list = response.xpath('//*[@id="content"]/div/div[2]')
        # 存储所有解析到的数据
        all_data = []
        for div in div_list:
            # 用户昵称
            author = div.xpath('./div/div[1]/a[2]/h2/text()').extract()
            author = ''.join(author)
            # 发表的内容
            # 列表调用extract之后,则表示将列表中的每一个selector对象中的data对应的数据字符串提取
            content = div.xpath('./div/a[1]/div/span//text()').extract()
            content = ''.join(content)
            # print(author,content)
        #     dic = {
        #         'author':author,
        #         'content':content
        #     }
        #     all_data.append(dic)
        # return all_data   

        # 基于管道
            item = TestprojectItem()
            item['author'] = author           
            item['content'] = content
        
            yield item #将item提交给管道
