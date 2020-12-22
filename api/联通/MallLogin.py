# -*- encoding: utf-8 -*-
'''
@文件    :MallLogin.py
@说明    :
@时间    :2020/12/18 15:06:41
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
import random
api = 'https://uac.10010.com/portal/Service/MallLogin'

headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'SHOP_PROV_CITY=; CaptchaCode=zLuK3veOwaLuBKjiMD7ub+ZWW5v2MhD16TSJ0MJ9h9s=; UID=uOKPrHvzb6avS14BGuteqtMEQnqPUdEo; WT_FPC=id=268ee0b80caeef2239a1608269361805:lv=1608269382083:ss=1608269361805; ckuuid=c81845159700faadf17362e4b3ff1879; cien=; userprocode=051; WT=13265547087; guide=true; upay_user=270ca16d177e069c5c014f3f7203e13a; mallcity=51|510; citycode=510; unisecid=512E04E482B2DD26E4CEC780A036987A; acw_tc=78f1209616082865294754028e75e602ef8c827d30e94637974f31dfdc; uacverifykey=ccn9929e8e8a3b03201fc309a072034878cgvy',
    'pragma': 'no-cache',
    'referer': 'https://uac.10010.com/portal/custLogin',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'corss',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
cc = int(time.time() * 1000)
cc+=1
expando = "jQuery"+('1.7.2'+ str(random.random())).replace('.', '')
""" f.ajaxSetup({
    jsonp: "callback",
    jsonpCallback: function() {
        return $.expando + "_" + $.now()++
    }
}), """

params = {
    #expando:"jQuery"+(jQuery.fn.jquery+Math.random()).replace(/\D/g,"")
    #$.expando
    "callback": "%s_%s" % (expando,cc),
    #req_time="+new Date().getTime()
    "req_time": '%s' % int(time.time() * 1000),
    "redirectURL": "https://upay.10010.com/npfweb/npfcellweb/phone_recharge_fill.htm",
    "userName": '13265547087',
    # var RSAUtils = $w.RSAUtils = {};
    #var key = RSAUtils.getKeyPair('11', '', '82fd84c464ab864897660ec64bafc32b998b60d5713dd57177820da7cf2409836b4506aa5c2b2943e701b6810df16da0b47e96274765aaf2d72152c5ca76d796756ec8c496cf4365c350c52312368e0c8c5504a14b1122bbde9c0f05627f33eb05ad52ea1f2c8ca7cf6a68e4ee9eee6b45773dc11fe830778202c8209d2ffaab');
    #params.password = RSAUtils.encryptedString(key, $("#userPwd").val().trim());
    "password": '03d14777b59ef7111e3a2d409d5814d92532fe2625c30ea316b92fb725690c12428d58823630e3339045ff73be03b01555584d8b0a39d75d65e9ae8b78167a73c1188796e8fe3f2388f84ee75042ca1356b16ce2e31e0aec619dcb59cd6d211adff5',
    "pwdType": "01",
    "productType": "01",
    # "verifyCode": "mx37", #验证码
    "uvc": "ccn9929e8e8a3b03201fc309a072034878cgvy",
    "redirectType": "01",
    "rememberMe": "1",
    "_": '%s' % int(time.time() * 1000 + int(random.random() * 10 + 1)) 
}
# jQuery17209065923354334071_1608276120336({resultCode:"0000",redirectURL:"https://upay.10010.com/npfweb/npfcellweb/phone_recharge_fill.htm"});
session = requests.session()
response = session.get(url=api, params=params, headers=headers)
info = response.text
if '验证码错误' in info:
    print('验证码错误')
elif "0000" in info:
    print('登录成功！！！')

