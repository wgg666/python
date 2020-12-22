# coding=utf-8
import random
import string


def Generate_domain_name():
    # 字母数字列表
    Alphanumeric_list = [str(i) for i in range(10)] * 5 + list(string.ascii_uppercase.lower()) * 5
    # 随机生成2~8位域名
    Alphanumeric_random = random.sample(Alphanumeric_list, random.randint(2, 8))
    # 域名列表转字符串
    Alphanumeric_str = ''.join(Alphanumeric_random)
    domain_name = f'https://www.{Alphanumeric_str}.com'
    return domain_name


if __name__ == '__main__':
    print(Generate_domain_name())
