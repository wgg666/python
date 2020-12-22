#coding=utf-8

import random
import hashlib

def moke_md5(string:str):
    #编码成bytes
    string = string.encode('utf-8')
    #MD5加密得到32位的16进制字符串
    md5 = hashlib.md5(string).hexdigest() #返回摘要
    return md5
print(moke_md5(''))
