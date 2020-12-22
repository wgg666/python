# -*- encoding: utf-8 -*-
'''
@文件    :凯撒加密.py
@说明    :
@时间    :2020/12/17 14:20:52
@作者    :AwAit
@版本    :1.0
'''

ptxt = input('请输入一串字符串：')
for c in ptxt:
    if 'a' <= c <= 'z':
        print(chr(ord('a') + (ord(c) - ord('a') + 4) % 26), end='')
    elif 'A' <= c <= 'Z':
        print(chr(ord('A') + (ord(c) - ord('A') + 4) % 26), end='')
    else:
        print(c, end='')