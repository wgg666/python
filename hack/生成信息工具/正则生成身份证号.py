# coding=utf-8
import random
import re
import json

def check_sfz_last(digs:str) -> str:
    """ 
    check_sfz_last  校验身份证最后一位
    :digs   身份证前17位
    """
    #校验码
    Check_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    #加权因子
    Weighting_factor = [7, 9, 10, 5, 8, 4, 2,1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # digs = input('身份证前17位: ')
    # isdigit检测字符串是否只由数字组成。
    if len(digs) != 17 or digs.isdigit() == False:
        print('incorrect input')
    else:
        return Check_list[sum([int(digs[i]) * Weighting_factor[i] for i in range(17)]) % 11]


# 6位数字地址码，8位数字出生日期码，3位数字顺序码和1位数字校验码
def generate_sfz(sfz_num):
    with open(r'.\hack\生成信息工具\身份证前6位.json','r',encoding='UTF-8') as f:
        data = json.load(f)
    # print(len(data))
    sfz6 = random.choice(list(data.keys()))
    IDRe18 = re.compile(
                        r'^(((18|19)\d{2})|2020)'  # 年
                        r'((0[1-9])|10|11|12)'  # 月
                        r'(([0-2][1-9])|10|20|30|31)'  # 日
                        r'\d{3}$'  # 数字顺序码
                        )  
    """ 
    r'^('
    r'(([1][1-5])|(2[1-3])|(3[1-7])|(4[1-6])|(5[0-4])|(6[1-5])|(71|81|82))'  # 前两位
    r'(([0][1-9])|([2-6][0-9])|70)'  # 3，4地级市（自治州）
    r')'
    r'(([0][1-9])|([1][0-8])|([2][1-9])|([3-9][0-9]))'  # 5，6区（县、自治县、县级市）
     """
    # r'[0-9Xx]'数字校验码

    IDre15 = r'^([1-6][1-9]|50)\d{4}\d{2}((0[1-9])|10|11|12)(([0-2][1-9])|10|20|30|31)\d{3}$'
    sfz_list = []
    # result = re.compile(IDRe18)
    while True:
        sfz11 = str(random.randint(10000000000, 99999999999))
        if IDRe18.findall(sfz11):
            sfz17 = sfz6 + sfz11
            check_code = check_sfz_last(sfz17)
            sfz = sfz17 + check_code 
            sfz_list.append(sfz)
            if len(sfz_list) == sfz_num:
                break
    
    return sfz_list


if __name__ == '__main__':
    pass
    sfz_num = int(input('请输入生成的身份证数量：'))
    for i in generate_sfz(sfz_num):
        print(i)
