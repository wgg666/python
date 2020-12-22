from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
    host = 'https://www.shicimingju.com'
    url = host + '/book/sanguoyanyi.html'
    # 请求头
    headers = {
        #请求载体的身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        #连接：保持活动
        "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9"
    }
    openmode = 'w'
    file = '.\\爬虫\\novel\\sanguoyanyi.txt'
    response_get = requests.get(url=url,headers=headers)
    # 响应的键值对
    def xy_item(response):
        headers_list = {
            "状态码":response.status_code,
            "内容类型":response.headers["Content-Type"],
            "服务器中间件":response.headers["Server"]
        }
        print(headers_list)
    xy_item(response_get)

    page_text = response_get.text
    soup = BeautifulSoup(page_text,'lxml')
    # 获取所有章节
    li_list = soup.select('.book-mulu > ul > li')
    # for li_list in li_list:
    #     print(li_list.text)
    fp = open(file,openmode,encoding='utf-8')
    for li in li_list:
        #a标签的文字
        title = li.a.string
        # 完整的a标签href
        detail_url = host + li.a['href']

        response_get = requests.get(url=detail_url,headers=headers)
        # 响应的键值对
        xy_item(response_get)
        # 拿到每个章节的所有内容
        detail_page_text = response_get.text
        # print(detail_page_text)
        # 解析所有章节对应的小说内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_="chapter_content")
        # 拿到所有章节对应的小说内容
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title,'下载成功！！！')
