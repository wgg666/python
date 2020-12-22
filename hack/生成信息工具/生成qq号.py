# coding=utf-8
import random
import re


# 1.// 判断是不是QQ号
# 2.// 1 首位不能是0  ^[1-9]
# 3.// 2 必须是 [5, 11] 位的数字 \d{4, 9}
def generate_qq(qq_num):
    qq_list = []
    while True:
        qq = str(random.randint(10000, 99999999999))
        result = re.compile(r'^[1-9][0-9]{4,10}$')
        if result.findall(qq):
            qq_list.append(qq)
            if len(qq_list) == qq_num:
                break
    return qq_list


if __name__ == '__main__':
    qq_num = int(input('想生成多少个QQ？'))
    for i in generate_qq(qq_num):
        print(i)
