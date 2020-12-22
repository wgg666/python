# coding=utf-8
import json

# from 爬虫.py.headers import getheaders
# from 爬虫.py.response import xy_item
import requests, parsel, time, random, threading, os, sys
from concurrent.futures import ThreadPoolExecutor

'''response_get = requests.get(
    url='http://www.ccb.com/cn/OtherResource/bankroll/html/code_help.html',
    headers=getheaders(1), verify=False)
xy_item(response_get)
data = response_get.text
# 解析
# 转化成selector对象
html_data = parsel.Selector(data)
# 拿到所有省份div
tbody_list = html_data.xpath('//*[@id="content"]/div/div')
province_list = []
for tr in tbody_list:
    province = tr.xpath('./h3/text()').extract_first()  # 省份
    Area_code = tr.xpath('.//td[1]/text()').re('\d\d\d\d')  # 地区代码
    District_Name = tr.xpath('.//td[2]/text()').re('[\u4e00-\u9fa5]{2,11}')  # 地区名称
    # 全国地区代码表
    province_list.append(province)
    province_list.append(Area_code)
    province_list.append(District_Name)
jsonArr = json.dumps(province_list, ensure_ascii=False)'''


# print(jsonArr)
# 银行卡号整体为13-19位，其中前6位为发卡标识代码，最后1位为校验码，中间的为个人识别码。
# 银行卡号一般有五部分组成：发卡机构标识代码（BIN）、地区代码、卡种类码、顺序码、校验码。
# 第7-10位代表发卡地区，用于识别城市和网点
# 卡种类代码 第11位表示卡种类码
# 顺序码 第12-18位代码是顺序码，是发卡行编制的，可以理解为银行卡的编码顺序

# 这个方案错误率太高，成功的都是422开头的19位visa信用卡
def generate_Bank_card_number():
    # 第一位
    Debit_Card_1 = [4, 5, 6, 9][random.randint(0, 3)]
    # 第2位
    Debit_Card_2 = [0, 2][random.randint(0, 1)]
    with open("全国地区代码表.json", 'r') as load_f:
        load_dict = json.load(load_f)
        # 天津
        tianjin = load_dict[1]
        # 辽宁
        liaoning = load_dict[4]
        shanghai = load_dict[7]  # 上海
        jiangsu = load_dict[10]  # 江苏
        shandon = load_dict[13]  # 山东
        hubei = load_dict[16]  # 湖北
        guangdon = load_dict[19]  # 广东
        shichuan = load_dict[22]  # 四川
        ninxia = load_dict[25]  # 宁夏
        shanxi = load_dict[28]  # 陕西
        beijin = load_dict[31]  # 北京
        chonqing = load_dict[34]  # 重庆
        hebei = load_dict[37]  # 河北
        Shanxi_Province = load_dict[40]  # 山西
        neimengu = load_dict[43]  # 内蒙古
        heilonjiang = load_dict[46]  # 黑龙江
        hainan = load_dict[49]  # 海南
        jilin = load_dict[52]  # 吉林
        zhejiang = load_dict[55]  # 浙江
        fujian = load_dict[58]  # 福建
        anhui = load_dict[61]  # 安徽
        henan = load_dict[64]  # 河南
        hunan = load_dict[67]  # 湖南
        jianxi = load_dict[70]  # 江西
        guanxi = load_dict[73]  # 广西
        yunnan = load_dict[76]  # 云南
        guizhou = load_dict[79]  # 贵州
        xizhan = load_dict[82]  # 西藏
        gansu = load_dict[85]  # 甘肃
        qinghai = load_dict[88]  # 青海
        xinjiang = load_dict[91]  # 新疆
        code_list = tianjin + liaoning + shanghai + jiangsu + shandon + hubei \
                    + guangdon + shichuan + ninxia + shanxi + beijin + chonqing + hebei + \
                    Shanxi_Province + neimengu + heilonjiang + hainan + jilin + zhejiang + anhui + fujian + \
                    henan + hunan + jianxi + guanxi + yunnan + guizhou + xizhan + gansu + qinghai + xinjiang
        # 7~10位
        duplicate_removal_code = list(set(code_list))[random.randint(0, 2141)]
        Bank_card_number = (f'{Debit_Card_1}{Debit_Card_2}{random.randint(1000, 9999)} {duplicate_removal_code} '
                            f'{random.randint(100, 999999999)}')
        return Bank_card_number


if __name__ == '__main__':
    Bank_card_number = generate_Bank_card_number()
    print(Bank_card_number)
