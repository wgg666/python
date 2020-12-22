# coding=utf-8
from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则表达式，文字匹配
import urllib.request,urllib.error  #指定url，获取网页数据
import xlwt #进行excel操作
import sqlite3  #进行sqlite数据库操作

def main():
    #1.爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    # 拿到数据
    datalist = getData(baseurl)
    # 保存的路径
    savepath = ".\\豆瓣电影Top250.xls"
    # 开始保存
    # saveData(savepath)
    # askURL("https://movie.douban.com/top250?start=0")

    #2.解析数据

def getData(baseurl):
    datalist = []
    for i in range(0,10):#10次
        url = baseurl + str(i*25)#1次25条
        html = askURL(url)
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            print(item)
    return datalist

#得到指定一个url的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

    #3.保存数据

def saveData(savepath):
    print("save....")

# 当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行
if __name__ == "__main__":
    main() #最后执行