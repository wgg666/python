# coding=utf-8
import random

'''
18位身份证号码用一个通式“ssqqxxyyyymmddnnnj”
6位数字地址码，8位数字出生日期码，3位数字顺序码和1位数字校验码
前1、2位数字表示：所在省（直辖市、自治区）的代码；11~82 
不包括16~20、24~30、38~40、47~49、55~60、66~70、72~80

第3、4位数字表示：所在地级市（自治州）的代码；
01-20，51-70表示省直辖市；21-50表示地区（自治州、盟）

第5、6位数字表示：所在区（县、自治县、县级市）的代码；
01-18表示市辖区或地区（自治州、盟）辖县级市；21-80表示县（旗）；81-99表示省直辖县级市。

第7—14位数字表示：出生年、月、日；
第15、16位数字表示：所在地的派出所的代码；
第17位数字表示性别：奇数表示男性，偶数表示女性；
18位：0~9 x
'''


def generate_sfz():
    # 前两位
    sfzss = [i for i in range(11, 83)
             if i not in range(16, 21)
             and i not in range(24, 31)
             and i not in range(38, 41)
             and i not in range(47, 50)
             and i not in range(55, 61)
             and i not in range(66, 71)
             and i not in range(72, 81)
             ][random.randint(0, 33)]
    # print(sfzss)

    # 3、4位
    sfzqq = [i for i in range(1, 71)][random.randint(0, 69)]
    if sfzqq in range(1, 10):
        sfzqq = '0' + str(sfzqq)
    # print(sfzqq)

    # 5、6位
    sfzxx = [i for i in range(1, 100) if i not in range(19, 21)][random.randint(0, 96)]
    if sfzxx in range(1, 10):
        sfzxx = '0' + str(sfzxx)
    # print(sfzxx)

    # 几几年
    sfzyyy = random.randint(1878, 2020)
    # print(sfzyyy)

    # 几月
    sfzmm = [i for i in range(1, 13)][random.randint(0, 11)]
    if sfzmm in range(1, 10):
        sfzmm = '0' + str(sfzmm)

    # 日
    sfzdd = [i for i in range(1, 32)][random.randint(0, 31)]
    if sfzdd in range(1, 10):
        sfzdd = '0' + str(sfzdd)
    # print(sfzdd)

    # 最后一位
    sfz18 = random.randint(0, 10)
    if sfz18 == 10:
        sfz18 = 'x'
    sfz = f'{sfzss}{sfzqq}{sfzxx} {sfzyyy}{sfzmm}{sfzdd} {random.randint(100, 999)} {sfz18}'
    return sfz


if __name__ == '__main__':
    sfz = generate_sfz()
    print(sfz)
