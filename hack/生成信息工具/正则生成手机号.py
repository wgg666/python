# coding=utf-8
import re
import random
import sys

import phone


# 第二位：3，4，5，7，8
# 第三位：根据第二位的数字对应生成的规律
# 3:0-9   4:5-9  5:没有4    7:没有9  8:0-9

def generate_phone(phone_num):
    phone_list = []
    result = re.compile(r'^[1]('
                        r'([3][0-9])|'
                        r'([4][5-9])|'
                        r'([5][0-3,5-9])|'
                        r'([6][5,6])|'
                        r'([7][0-8])|'
                        r'([8][0-9])|'
                        r'([9][1,8,9])'
                        r')[0-9]{8}$')
    while True:
        sjh = str(random.randint(10000000000, 99999999999))
        if result.findall(sjh):
            phone_list.append(sjh)
            if len(phone_list) == phone_num:
                break
    return phone_list


# 查询手机号信息
def location(phone_number):
    p = phone.Phone()
    result = p.find(phone_number)
    return result


if __name__ == '__main__':
    phone_num = int(input('请输入生成的手机号数量：'))
    for i in generate_phone(phone_num):
        print(location(i))
    print(location('13265547087'))