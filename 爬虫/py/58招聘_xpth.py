from lxml import etree
import requests
if __name__ == "__main__":
    openmode = 'a+'
    file = '.\\爬虫\\work\\58招聘廉江.txt'
    url = 'https://zhanjiang.58.com/lianjiang/job/'
    urls = 'https://zhanjiang.58.com/lianjiang/job/pn%d'
    # 遍历所有下一页
    for pageNum in range(1, 62):
        # 对应页码的url
        new_url = format(urls % pageNum)
        hmpages = new_url.split('/')[-1]
        # 请求头
        headers = {
            # 请求载体的身份信息
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            # 连接：保持活动
            "Connection": "keep-alive",
            "accept-language": "zh-CN,zh;q=0.9"
        }
        response_get = requests.get(url=new_url, headers=headers)
        # 响应的键值对

        def xy_item(response):
            headers_list = {
                "状态码": response.status_code,
                "内容类型": response.headers["Content-Type"],
                "服务器中间件": response.headers["Server"]
            }
            print(headers_list)
        xy_item(response_get)

        # html页面
        page_text = response_get.text
        # 解析html
        tree = etree.HTML(page_text)

        li_list = tree.xpath('//*[@id="list_con"]/li')
        fp = open(file, openmode, encoding='utf-8')
        for li in li_list:
            job_item = li.xpath('./div//text()')
            # print(job_item)
            fp.write(str(job_item) + '\n')
            print(hmpages,'已爬取')
