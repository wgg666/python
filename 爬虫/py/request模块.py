import requests
import os
import json

if __name__ == "__main__":
    writemode = 'w'
    # 请求关键词参数
    # kw = input('关键词：')
    param = {
        # 'query':
        # "type": '24',
        # "interval_id": '100:90',
        # "action": '',
        # "start": '0',
        # "limit": '20'
    }
    url = 'https://movie.douban.com/j/chart/top_list'
    
    # 获取当前文件所在目录
    # filename = f'{os.path.dirname(__file__)}\\shuju\\{kw}.html'
    jsonname = f'{os.path.dirname(__file__)}\\shuju\\douban.json'
    # 请求头
    headers = {
        #请求载体的身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        #连接：保持活动
        "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9"
    }

    # 发起get请求
    response_get = requests.get(url=url,params=param,headers=headers)
    # 响应的键值对
    def xy_item(response):
        headers_list = {
            "状态码":response.status_code,
            "内容类型":response.headers["Content-Type"],
            "服务器中间件":response.headers["Server"]
            }
        for item in headers_list:
            print(item,headers_list[item],sep='：')
    xy_item(response_get)
    # html页面
    # page_text = response_get.text
    # print(page_text)
    # 获取电影json列表
    # list_data = response_get.json()
    # 写入json
    # with open(jsonname,writemode,encoding='utf-8') as fp:
    #     json.dump(list_data,fp=fp,ensure_ascii=False)
    #     print('over!')
   
    # 数据写入文件
    # with open(filename,writemode,encoding='utf-8') as fp:
    #     fp.write(page_text)
    # print(filename,'保存成功！！！','爬取数据结束！')

    # post请求
"""     post_url = "https://fanyi.baidu.com/v2transapi"
    word = input('enter a word：')
    jsonname = f'{os.path.dirname(__file__)}\\shuju\\{word}.json'
    data = {
        'from': 'zh',
        'to': 'en',
        # 'query': word,
        "transtype": "realtime",
        "simple_means_flag": "3",
        'sign': "967445.663588",
        "token": "9e4eef3c70d087f1de9a16a865b8ec0f",
        "domain": "common"
    }
    headers = {
        "accept": "*/*",
        #接受编码
        "accept-encoding": "gzip, deflate, br",
        # # 内容长度
        # "content-Length": "121",
        # 内容类型
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        #请求载体的身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        #连接：保持活动
        "Connection": "keep-alive",
        # 接受语言
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "PSTM=1602005082; BIDUPSID=76D2AB00950B031ABD5C39B3F178FB59; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=9E38769FACCFABACD29C184D1A746847:FG=1; BDUSS=g5NXBmemxEUUgydTg3QXplWVh2VmstUHIwMmljaDZERUdWbExIcDRXaWc4YnhmRVFBQUFBJCQAAAAAAAAAAAEAAABXfLWuV0cxMzI2NTU0NzA4NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKBklV-gZJVfdD; BDUSS_BFESS=g5NXBmemxEUUgydTg3QXplWVh2VmstUHIwMmljaDZERUdWbExIcDRXaWc4YnhmRVFBQUFBJCQAAAAAAAAAAAEAAABXfLWuV0cxMzI2NTU0NzA4NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKBklV-gZJVfdD; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1604388994,1604472973,1604639616,1604905339; H_PS_PSSID=32817_1460_32854_33059_31254_32706_32962; delPer=0; PSINO=7; yjs_js_security_passport=ae01dfd8206ad97fb4c260e1ecec148d49830005_1605012761_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1605012567; __yjsv5_shitong=1.0_7_fb2039b48b9a247dc04152a17a38895f9250_300_1605012771151_120.239.146.94_3269ffe1",
        # 起源
        "origin": "https://fanyi.baidu.com",
        "referer": "https://fanyi.baidu.com/",
        # 秒-获取-目的地
        "sec-fetch-dest": "empty",
        # 秒获取模式
        "sec-fetch-mode": "cors",
        # 获取站点
        "sec-fetch-site": "same-origin",
        # x-请求-带:XML Http请求
        "x-requested-with": "XMLHttpRequest",
    }

    response_post = requests.post(url=post_url,data=data,headers=headers)
    dic_obj = response_post.json()
    xy_item(response_post)
    # print(dic_obj)

    #持久化存储
    fp = open(jsonname,writemode,encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over!!!') """