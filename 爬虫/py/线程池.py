import requests,json,time,re,random
from urllib.parse import urlparse
from multiprocessing.dummy import Pool
from lxml import etree

mp4_file = '.\\爬虫\\mp4\\'
start_time = time.time()
videomode = 'wb'
url = 'https://www.pearvideo.com/category_5'
headers = {
    # 请求载体的身份信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # 连接：保持活动
    "Connection": "keep-alive",
    "accept-language": "zh-CN,zh;q=0.9"
}
response_get = requests.get(url=url, headers=headers)
# 响应的键值对

def xy_item(response):
    headers_list = {
        "状态码": response.status_code,
        "内容类型": response.headers["Content-Type"],
        # "服务器中间件": response.headers["Server"]
    }
    print(headers_list)
xy_item(response_get)
# 生活板块的页面
page_text = response_get.text
tree = etree.HTML(page_text)
# 拿到4个li
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
# 存储所有视频链接
urls = []
for li in li_list:
    # 视频播放地址
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    # print(detail_url,name)
    # 视频的页面
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    # 解析视频地址
    # ex = 'srcUrl="(.*?)",vdoUrl'
    # video_url = re.findall(ex,detail_page_text)[0]
    """ 
    https://www.pearvideo.com/js/post.js?v=4.90
    data    :   "parentId="1667549"
    &score=" + next_score + "
    &myinfoId=" "
    &postUserId=10008579
    &pageidx=" + pageidx + filterIds +"
    &mrd=" + Math.random(),

    data	:	"parentId=" + _commId + "
    &score=" + next_score + "
    &myinfoId=" + myinfoId + "
    &postUserId=" + postUserId + "
    &mrd=" + Math.random(),


    postId = "1667549"
    cont-       contId = "1706794" 
    -           postUserId = "10008579"
    -           
    hd
    mrd="+Math.random()

    https://www.pearvideo.com/videoStatus.jsp?contId=1706794&mrd=0.36277974146092173
     """
    contId = detail_url.split('_')[-1]
    headers = {
        # 请求载体的身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        # 连接：保持活动
        "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "PEAR_UUID=c8341dff-8470-44f0-81af-521401413865; _uab_collina=160524479322240045528941; UM_distinctid=175c00bc69e15e-0a96afaa7d6ac1-4353760-e1000-175c00bc6a1f7; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1605244799; __secdyid=53bf4c59dd39e63070f61c745603ba8f78ef924002be9bbf021605249444; p_h5_u=DB298AE1-B2C8-4E0E-A47C-FCB36E62EA41; acw_tc=76b20f6016052647418827000e5ebf5b19f5b9d15fcdad787b266da200726d; JSESSIONID=4F1A73F7329FFEF06159AC81DDC4896C; CNZZDATA1260553744=1226175696-1605244611-https%253A%252F%252Fwww.baidu.com%252F%7C1605260896; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1605265827; SERVERID=a7cc60ddba048546c9441d2558c201d4|1605266049|1605264741",
        "Host": "www.pearvideo.com",
        "Referer": "https://www.pearvideo.com/video_" + contId,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-Requested-With": "XMLHttpRequest"
    }

    # print(contId)
#     # 视频接口列表
    video_jk_list = 'https://www.pearvideo.com/videoStatus.jsp?contId=' + contId + '&mrd=' + str(random.random())
    # print(video_jk_list)
    response_get = requests.get(url=video_jk_list,headers=headers)
    xy_item(response_get)
    # print(response_get.text)
    # https://video.pearvideo.com/mp4/third/20201113/1605257347980-10008579-101439-hd.mp4
    # 加密的4个视频地址
    jm_srcUrl = json.loads(response_get.text).get('videoInfo').get('videos').get('srcUrl')
    parsed = urlparse(jm_srcUrl)
    # https://video.pearvideo.com/mp4/third/20201113/
    srcUrl_2 = parsed.path.rsplit('/')[4].rsplit('-')
    # 10008579-101439-hd.mp4
    srcUrl_3 = srcUrl_2[1] + '-' + srcUrl_2[2] + '-' + srcUrl_2[3]
    # 4个视频的地址
    srcUrl = parsed.scheme + '://'\
     + parsed.netloc + '/' \
     + parsed.path.rsplit('/')[1] \
     + '/' + parsed.path.rsplit('/')[2] \
     + '/' + parsed.path.rsplit('/')[3] \
     + '/' + 'cont-' + contId + '-' + srcUrl_3
    # print(srcUrl)
    # 存储视频名字和地址
    dic = {
        'name':name,
        'url':srcUrl
    }
    urls.append(dic)

    headers = {
        # 请求载体的身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        # 连接：保持活动
        "Connection": "keep-alive",
        "cookie": "PEAR_UUID=c8341dff-8470-44f0-81af-521401413865; UM_distinctid=175c00bc69e15e-0a96afaa7d6ac1-4353760-e1000-175c00bc6a1f7; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1605244799; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1605281356",
    }

def get_video_data(dic):
    url = dic['url']
    response_get = requests.get(url=url,headers=headers)
    xy_item(response_get)
    # 4个视频数据
    data = response_get.content
    print(dic['name'],'正在下载')
    with open(mp4_file + dic['name'],videomode) as fp:
        fp.write(data)
        print(dic['name'],'下载ok！！！')
# 使用线程池对视频数据进行请求
pool = Pool(4)
pool.map(get_video_data,urls)
# print(urls)
# 关闭pool，使其不在接受新的（主进程）任务
pool.close()
# 是说：主进程阻塞后，让子进程继续运行完成，子进程运行完后，再把主进程全部关掉。
pool.join()
end_time = time.time()
print('耗时:%s秒' % (end_time - start_time))