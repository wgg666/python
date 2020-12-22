# coding=utf-8
import random
import phone

'''
规则：11位
第一位：1开头
第二位：3，4，5，7，8
第三位：根据第二位的数字对应生成的规律 
3:0-9   4:5-9  5:没有4    7:没有9  8:0-9
后八位：随机生成8个数字
'''


def generate_phone():
    # 第二位
    sec = [3, 4, 5, 7, 8][random.randint(0, 4)]
    th = {
        3: random.randint(0, 9),
        4: random.randint(5, 9),
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(0, 9)][random.randint(0, 8)],
        8: random.randint(0, 9)
    }[sec]
    # 后八位数
    end = str(random.randint(10000000, 99999999))  # 随机生成8位
    phone = f'1{sec}{th}{end}'
    return phone


# 查询手机号信息
def location(phone_number):
    p = phone.Phone()
    result = p.find(phone_number)
    return result


if __name__ == '__main__':
    # print(generate_phone())
    print(location(generate_phone()))
