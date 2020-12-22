import threading
import socket
import unicodedata
import PIL.ImageOps
from pytesseract import *
import pytesseract
from random import *
import os
import sys
from 爬虫.py.chaojiying import Chaojiying_Client
from requests.models import Response
from 爬虫.py.response import xy_item
import requests
from 爬虫.py.headers import getheaders
import cv2 as cv
from matplotlib.pyplot import cla, text
import pytesseract as tess
from matplotlib import pyplot as plt
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
import re
import hashlib
import rsa
import base64
import execjs
import uuid
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

class Chrome_Options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options_lists = [
        "--no-sandbox",  # 加上这句,就不会报崩溃了
        '--ignore-certificate-errors',  # 忽略证书错误
        # '--headless',# 无头
        '--disable-gpu',  # 禁用-gpu#规避bug
        'User-Agent="%s"' % 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    ]
    for chrome_options_list in chrome_options_lists:
        chrome_options.add_argument(chrome_options_list)
    # 排除开关启用自动操作设置为开发者模式，防止被各大网站识别出来使用了Selenium
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-automation'])
chrome_options = Chrome_Options().chrome_options
# driver = webdriver.Chrome(chrome_options=chrome_options)
# print(chrome_options._arguments)
# print(chrome_options._experimental_options)

def RSAencode(_str:str,pubk:str):
    """ 
    RSA公钥加密 
    :_str    加密的字符串
    :pubk   公钥
    """
    # 获取cookie的'_pubk'的值
    #把base64解码成16进制bytes公钥 b'\x...'
    # public_key = base64.b64decode(pubk)
    #导入公钥
    rsakey = RSA.importKey(pubk)
    # 字符串转成bytes
    #用公钥加密bytes得到的是16进制bytes b'\x...'
    crypto = rsa.encrypt(_str.encode(), rsakey)
    # 把16进制bytes转256位16进制数（字符串）
    return crypto.hex()
key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC/M868kojjC5nTlW2VAXwWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh/Yqtv8eTpRQq6TCMyaU8u/vj5rZsqFR7wEOEL+zDdt7Xr/n7aoOwRDMYRPdnxV5PwyDLYrVGX4/x4+SxcpbflgchjPHx10ubEd7KM2QIDAQAB'
publicKey = '-----BEGIN RSA PUBLIC KEY-----\n' + key + '\n-----END RSA PUBLIC KEY-----'
print(len(RSAencode('13265547087',publicKey)))