# -*- encoding: utf-8 -*-
'''
@文件    :判断生肖.py
@说明    :
@时间    :2020/12/20 17:12:32
@作者    :AwAit
@版本    :1.0
'''
from datetime import datetime
def get_zodiac(birth_year:int) -> str:
    """ 
    获取生肖
    :birth_year   出生年份
    """
    All_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
    if type(birth_year) == str:
        birth_year = int(birth_year)

    zodiac = All_zodiac[(birth_year - datetime.now().year) % 12]
    return zodiac

if __name__ == "__main__":
    print(get_zodiac('2000'))