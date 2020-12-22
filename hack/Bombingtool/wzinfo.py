import sys
from 数据相关.正则表达式.请求头加引号 import add_yinhao

data = {
    # 不需要识别验证码直接请求验证码api
    "巨人账号": {
        'url': 'https://reg.ztgame.com/common/sendmpcode',
        'headers': {
            "Cookie": "_ee70c=http://172.28.198.75:80; AM_SESSID=c4k1qb8orpq8d2n73j7pnqp7ti; ucd=4d505229901fb8499ae203ae2359818006a5a1dff0e8b30718015822b5a20ec1a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ucd%22%3Bi%3A1%3Bs%3A26%3A%22c4k1qb8orpq8d2n73j7pnqp7ti%22%3B%7D; NSC_l8t-usbfgjl-ttm-pomjof-UY-J=ffffffffaf14d61745525d5f4f58455e445a4a426d90; UM_distinctid=1760eaf9eec28f-0e90620fabc8f2-4353760-e1000-1760eaf9ef429; uniqid=2011281953144000529456; ref=0; ref_date=2020-11-28+19%3A53%3A14.0144; ref_ip=120.231.15.57; CNZZDATA1262808196=1231874534-1606559164-https%253A%252F%252Fwww.baidu.com%252F%7C1606564617; date=2020-11-28+20%3A03%3A31.1401",
            "Host": "reg.ztgame.com",
            "Referer": "https://reg.ztgame.com/site/index?source=giant_site",
        }
    },
    '好大夫在线': {
        'url': 'https://passport.haodf.com/user/showregisterbymobile',
        '手机号输入框': {'xpath': '//*[@id="tel"]'},
        '验证码': {"xpath": '//*[@id="registercaptcha1"]'},
        '验证码输入框': {"xpath": '//*[@id="psw"]'},
        '发送验证码按钮': {"xpath": '/html/body/div[3]/div[2]/div/form/div[5]/div/a[1]'},
        '已发送5次文本': {"xpath": '/html/body/div[3]/div[2]/div/form/div[6]'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\haodaifu.png'}
    },
    # 不需要识别验证码直接获取到
    "方正飞翔": {
        'url': 'http://www.founderfx.cn/fxsso/login?service=http://www.founderfx.cn/staticpage/help_center.jhtml&_scope=1',
        '手机号输入框': {'xpath': '//*[@id="username_reg"]'},
        '验证码': {"xpath": '//*[@id="showCode"]'},
        '验证码输入框': {"xpath": '//*[@id="inputCode"]'},
        '发送验证码按钮': {"xpath": '//*[@id="btnSend"]'},
        "确定": {"xpath": '//*[@id="cas"]/div[3]/div[3]/a'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\haodaifu.png'}
    },
    # 不需要识别验证码直接请求验证码api
    "金游世界": {
        'url': 'http://reg.51v.cn/reg_client_M.aspx',
        'api': 'http://reg.51v.cn/ajaxpro/reg_client_M,App_Web_reg_client_m.aspx.cdcab7d2.ashx',
        '手机号输入框': {'xpath': '//*[@id="txtLoginName"]'},
        '验证码输入框': {"xpath": '//*[@id="txtMobileVcodeP"]'},
        '发送验证码': {"xpath": '//*[@id="getMobileCodeLink"]'},
    },
    #善见教育
    "全国中小学智慧教育云平台": {
        'url': 'http://www.30edu.com.cn/UserRegister.shtml',
        '手机号输入框': {'xpath': '//*[@id="Mobile"]'},
        '验证码': {"xpath": '//*[@id="userTab"]/li[15]/div[2]/img'},
        '验证码输入框': {"xpath": '//*[@id="VerifyCode"]'},
        '发送验证码按钮': {"xpath": '//*[@id="MobileCodeButton"]'},
        "图形码填写错误": {'xpath': '/html/body/div[7]/div/table/tbody/tr[2]/td/div'},
        "重新获取": {'xpath': '//*[@id="userTab"]/li[16]/div[2]/div[2]/a[2]/text()[1]'},
        "发送成功弹窗文本": {'xpath': '/html/body/div[7]/div/table/tbody/tr[2]/td/div'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\_30edu.png'}
    },
    "一路财富": {
        'url': 'https://www.yilucaifu.com/passport/reg.html',
        '手机号输入框': {'xpath': '//*[@id="js_username"]'},
        '验证码': {"xpath": '//*[@id="form"]/div[1]/div[2]/div/div/img'},
        '验证码输入框': {"xpath": '//*[@id="form"]/div[1]/div[2]/div/div/input'},
        '发送验证码按钮': {"xpath": '//*[@id="form"]/div[1]/div[3]/div/div/a'},
        "次数限制弹窗文本": {'xpath': '/html/body/div[7]/div/div[1]'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\yilucaifu.png'}
    },
    "乐居": {
        "url": "https://my.leju.com/settings/register/indexview",
        "手机号输入框": {"xpath": '//*[@id="registerForm"]/ul/li[1]/div/input'},
        '验证码输入框': {"xpath": '//*[@id="registerForm"]/ul/li[2]/div/div/input'},
        "验证码": {"xpath": '//*[@id="yz_num"]'},
        "发送验证码按钮": {"xpath": '//*[@id="registerForm"]/ul/li[3]/div/a'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\leju.png'}
    },
    # 不需要识别验证码直接发送验证码
    "酷狗音乐": {
        "url": "https://www.kugou.com/reg/web/",
        "api": "https://gateway.kugou.com/v8/send_mobile_code",
        "手机号输入框": {"xpath": '//*[@id="t02Mobile"]'},
        "验证码输入框": {'xpath': '//*[@id="t02Code"]'},
        "发送验证码按钮": {'xpath': '//*[@id="t02GetCode"]/span'}
    },
    # 不需要验证码直接post接口
    "耐克": {"api": "https://unite.nike.com/phoneVerification"},
    # 绕过验证码post接口,发送失败更新一下cookie
    "冰川网络": {
        "api": "https://passport.q1.com/Register/MobileRegisterVerifyCodeNew",
        "headers": {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "pflags=0; UM_distinctid=176271922537d-0fd2faa48e1fa-4353760-e1000-17627192254ea; sid=LdUIPhkR5gDYnbEK]O8]L2GYeANLdUIhxmokJx46SCaRulnmcTtJT48xEA==; CNZZDATA3132899=cnzz_eid%3D1229609947-1606969063-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1607059037; zy_lvp=/mobileregister.html",
            "origin": "https://passport.q1.com",
            "referer": "https://passport.q1.com/mobileregister.html",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        },
    },
    # 绕过验证码post接口
    "北京爱琴海乐之技术有限公司": {'api': "http://uc.inoteexpress.com/util/sendcode"},
    "昊嘉在线": {
        'url': "http://passport.hogacn.com/reg.ftl",
        "手机号输入框": {'xpath': '//*[@id="mobile_num"]'},
        '验证码输入框': {'xpath': '//*[@id="answer"]'},
        '验证码': {'xpath': '//*[@id="jianyanmaImg"]'},
        '发送验证码按钮': {'xpath': '//*[@id="btnVerifyCode"]'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\hogacn.png'}
    },
    # 正常300秒1次，可用请求接口,失败换cookie和data的验证码和key
    "蹦蹦网": {
        'url': 'http://www.bengbeng.com/reg1.html',
        'api': 'http://www.bengbeng.com/ajax.php',
        "手机号输入框": {"xpath": '//*[@id="tbUserCell"]'},
        "验证码输入框": {"xpath": '//*[@id="tbCode_cell"]'},
        '验证码': {'xpath': '//*[@id="tbCodeImg_cell"]'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\bengbeng.png'},
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "UM_distinctid=176282e879416c-0cfbccf0a10845-4353760-e1000-176282e87951a; __utmc=267949597; __utmz=267949597.1606991908.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; PHPSESSID=t8c26rf3qhcc5o561rf9o16fh2; CNZZDATA4974798=cnzz_eid%3D1038084948-1606989622-null%26ntime%3D1607060114; __utma=267949597.2061322581.1606991908.1606991908.1607064466.2; __utmt=1; __utmb=267949597.1.10.1607064466",
            "Host": "www.bengbeng.com",
            "Origin": "http://www.bengbeng.com",
            "Referer": "http://www.bengbeng.com/reg1.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
    },
    '360账号中心': {
        'url': "https://i.360.cn/reg/",
        '手机号输入框': {'xpath': '//*[@id="js-sdk"]/div/div[2]/div/div[1]/div/form/div[1]/div/div[1]/div/div[1]/div[2]/input'},
        '验证码输入框': {'xpath': '//*[@id="js-sdk"]/div/div[2]/div/div[1]/div/form/div[1]/div/div[2]/div/div/input'},
        '验证码': {'xpath': '//*[@id="js-sdk"]/div/div[2]/div/div[1]/div/form/div[1]/div/div[2]/div/img'},
        '发送验证码按钮': {'xpath': '//*[@id="js-sdk"]/div/div[2]/div/div[1]/div/form/div[1]/div/div[3]/div/div/div[2]/span'},
        # '该手机号已经注册': {'xpath':'//*[@id="js-sdk"]/div/div[2]/div/div[1]/div/form/div[1]/div/div[1]/div/div[2]'},
        # '验证码错误请重新输入':{'xpath':'//*[@id="js-sdk"]/div/div[2]/div/div[1]/div/form/div[1]/div/div[2]/div/div[2]'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\i360.png'}
    },
    "搜了网": {"api": "http://reg.51sole.com/reghandler.ashx"},
    #赫斯特中国
    'ELLE中文网':{
        'api':'http://passport.ellechina.com/misc.php?mod=seccode&action=mobiverify',
        "headers": {
            "Accept": "application/xml, text/xml, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "gpaH_d712_lastvisit=1607049603; gpaH_d712_sid=3dh5FS; __jsluid_h=462aa8093a5882c9d0f42a34d25680ea; _ga=GA1.3.2087416999.1607052970; _gid=GA1.3.1774182038.1607052970; Hm_lvt_2fd7fc162331a375a7aab2d3038defa0=1607052970; Hm_lpvt_2fd7fc162331a375a7aab2d3038defa0=1607052970; gpaH_d712_lastact=1607053221%09misc.php%09seccode; gpaH_d712_rgg_mvcct=MXww",
            "Host": "passport.ellechina.com",
            "Origin": "http://passport.ellechina.com",
            "Referer": "http://passport.ellechina.com/register",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        },
        "data":{
            "atype": "1",
            "rgloadt": "1607053203"
        }
    },
    "世纪佳缘交友网": {
        'api':'https://reg.jiayuan.com/libs/xajax/reguser.server.php?processGeetestVerify',
        "headers": {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-length": "380",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "SESSION_HASH=10195f6eeb182fd11e99834534722a3f97f9074e; accessID=20201204123743387887; user_access=1; PHPSESSID=0b37bf2df87dcf69ab2327b0aeb21dba; Qs_lvt_336351=1607056675; AGL_USER_ID=8b74b4d6-1361-4546-8750-c2014980c8a9; Qs_pv_336351=346836375122711600%2C3002979424022203400",
            "origin": "https://reg.jiayuan.com",
            "referer": "https://reg.jiayuan.com/signup/fillbasic.php?bd=210",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
    },
    '门口学习网':{
        'api':"http://menco.cn/api/verifications",
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json; charset=UTF-8",
            "Cookie": "PHPSESSID=3nd215d43c88401frkmau2fr64; YII_CSRF_TOKEN=a1e7abe63205ec27fdb08c1e404db9c872682dfe",
            "Host": "menco.cn",
            "Origin": "http://menco.cn",
            "Referer": "http://menco.cn/register",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "X-YII-CSRF-TOKEN": "a1e7abe63205ec27fdb08c1e404db9c872682dfe",
        }
    },
    #发送失败更换验证码
    "缙云游戏中心":{
        'url' : 'http://register.jy5188.com/',
        "api": {
            '发送短信验证码':'http://register.jy5188.com/MobileCode.ashx',
            '图片验证码': 'http://register.jy5188.com/VerifyCodeImg.aspx?t=NM'
        },
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "pkRegisterTool=UNID=1|UnionID=1|SiteID=1|TopUserID=0|RefUrl=|IfRef=False|SetupId=0|Annalid=0; ASP.NET_SessionId=yxbijc45civv5055ktyh50ev",
            "Host": "register.jy5188.com",
            "Origin": "http://register.jy5188.com",
            "Referer": "http://register.jy5188.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        },
        '验证码': {'xpath': '//*[@id="vcode_img"]'},
        'path':{'验证码': str(sys.path[0]) + '\\code\\jy5188.png'}
    },
    #新网
    "ICP备案系统": {
        'api': 'http://beian.xinnet.com/api/sms/send',
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "captcha" : '',
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "cs_id=55b6565d0a751d3e165cbea9cce743e0",
            "Host": "beian.xinnet.com",
            "Origin": "http://beian.xinnet.com",
            "Referer": "http://beian.xinnet.com/signup",
            'remember' : '',
            "token" : '',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        }
    },
    #发送失败更换cookie,data的vscode和msgPhoneKey
    "我的钢铁网": {
        'api': 'https://passport.mysteel.com/smsSendValidateServletByWangYi.jsp',
        'headers': {
            "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "__snaker__id=bvltaB87moXxBzaA; Hm_lvt_1c4432afacfa2301369a5625795031b8=1607060737; href=https%3A%2F%2Fpassport.mysteel.com%2Fjoin.jsp%3Fsite%3Dwww.mysteel.com; accessId=5d36a9e0-919c-11e9-903c-ab24dbab411b; _9755xjdesxxd_=32; YD00126731780350%3AWM_NI=EJkw9ni%2Bj05n2qlee0HbevAFmXcC%2BraJJSAFLcck4pieRRLnPvEysIcA97bT7Jn9SPMsSgQ6IvsSVJ1uVgKgo3QT1IdewDCVZ8lDh0QWYjWXLSixf1i%2BqqEpgf7eXwSuenk%3D; YD00126731780350%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed2f15ab7abb6dad080a7ef8ea6d45f978b9ebbaa6a82b7b8afe45483eeb996d02af0fea7c3b92a8796a598bc66abf5a6d1b866f2afa486e83c8cbeab97c44eaf88ada4aa7aa39686b4c44e90bdad8cb77cabbb9eb3cf6694aa8b9af243a19ff7d8e160f596a2dad25c8fad9d88d43e8baabdb4d542f3ab9a88ca6daded9fb5b443a8bbb9a5c25e9ae8a4a5eb3c9389978bd654908da799e53babf5bf92c87ca5baf986db7d91abab8fea37e2a3; YD00126731780350%3AWM_TID=w6lanksoaIJBFBAARFcrfVm1YbDB316N; qimo_seosource_5d36a9e0-919c-11e9-903c-ab24dbab411b=%E7%AB%99%E5%86%85; qimo_seokeywords_5d36a9e0-919c-11e9-903c-ab24dbab411b=; qimo_xstKeywords_5d36a9e0-919c-11e9-903c-ab24dbab411b=; JSESSIONID=D055EC9D5E81A6BE673958A7D4D75B62; Hm_lpvt_1c4432afacfa2301369a5625795031b8=1607069595; pageViewNum=4; gdxidpyhxdE=szZW%5C64jfrcDfCATPK2DeOqVhRyTbA4G9SbTON0%2Bd5jB5z6V0Dt24RshJbT2LfYoWclEGTzh3%2FdAkiXMQjCpLHXTHWpjeQdM9gPyT44E2Yl8bj%2BIWJ2t8p3UM4IC1eR%2FvI2qe1nuEWEPrcjvWsiKZ62SKEUza9m5rJdJ8oyPNp9%5C17G0%3A1607070495461",
            "Host": "passport.mysteel.com",
            "Origin": "https://passport.mysteel.com",
            "Referer": "https://passport.mysteel.com/join.jsp?site=passport.mysteel.com&callback=https://www.mysteel.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        },
    },
    "开店宝": {
        'api':'https://epassport.meituan.com/gw/login/sendSmsCode',
        "headers": {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "uuid=1b65bac5509394dacd18.1607060986.1.0.0; _lxsdk_cuid=1762c48fc04c8-04473b230df37e-4353760-e1000-1762c48fc0459; _lxsdk=1762c48fc04c8-04473b230df37e-4353760-e1000-1762c48fc0459; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=1762c48fc0b-a3f-398-2e9%7C%7C7",
            "Host": "epassport.meituan.com",
            "Origin": "https://epassport.meituan.com",
            "Referer": "https://epassport.meituan.com/new/login?service=com.sankuai.meishi.fe.ecom&bg_source=1&part_type=0&continue=https%3A%2F%2Fe.meituan.com%2Fmeishi%2Fepassport%2Ftoken%3Ftarget%3Dhttps%253A%252F%252Fe.meituan.com%252Fmeishi%252F&feconfig=bssoify&bizlogintoken=&leftBottomLink=&appkey=com.sankuai.meishi.fe.ecom&bgSource=1&partType=0&loginContinue=https%3A%2F%2Fe.meituan.com%2Fmeishi%2Fepassport%2Ftoken%3Ftarget%3Dhttps%253A%252F%252Fe.meituan.com%252Fmeishi%252F",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
    },
    "人人网": {
        'url': 'http://reg.renren.com/xn6218.do',
        'api': 'http://reg.renren.com/ajax-mobile-code-new.do',
        'headers': {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "anonymid=kia08qrp-99ee1h; taihe_bi_sdk_uid=1434838f4be97045d7442e5ef45c666a; taihe_bi_sdk_session=449a39e0b25a0ddd625c763002dc023a; ick=0a7c2706-7d17-4a73-b51b-b1bab69e781c",
            "Host": "reg.renren.com",
            "Origin": "http://reg.renren.com",
            "Referer": "http://reg.renren.com/xn6218.do",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        },
        '手机号输入框': {'xpath':'//*[@id="regMobile"]'},
        '密码输入框': {'xpath': '//*[@id="pwd"]'},
        '发送验证码按钮': {'xpath': '/html/body/div[5]/div[3]/div/button[2]/span'},
        '验证码': {'xpath': '/html/body/div[5]/div[2]/div/img'},
        '验证码输入框': {'xpath': '/html/body/div[5]/div[2]/div/input'},
        '伪发送验证码按钮':{'xpath': '//*[@id="btn_getcode"]'},
        '重新发送验证码按钮': {'xpath': '//*[@id="btn_getcode"]'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\renren.png'}
    },
    '豆瓣': {
        'api': 'https://accounts.douban.com/j/mobile/login/request_phone_code',
        'headers': {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": 'bid=ypK7RUxy7dc; ll="118288"; _vwo_uuid_v2=D956E07064E3E3AD6312B0C368392E606|7c6a5f15e7479c6bcb14d594f0bc5050; __gads=ID=d4fe3d7babd308e8-223aae53aac40071:T=1605026824:RT=1605026824:S=ALNI_MbSd1fNLpYiX_yRkO3e30KutrJl1Q; ap_v=0,6.0; __utmc=30149280; apiKey=; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1607085124%2C%22https%3A%2F%2Fmovie.douban.com%2Ftv%2F%22%5D; _pk_id.100001.2fad=941c08fdc7c9c4b9.1607078834.3.1607085124.1607080859.; _pk_ses.100001.2fad=*; login_start_time=1607085125753; __utma=30149280.651662777.1602305222.1607078829.1607085309.10; __utmb=30149280.0.10.1607085309; __utmz=30149280.1607085309.10.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
            "Host": "accounts.douban.com",
            "Origin": "https://accounts.douban.com",
            "Referer": "https://accounts.douban.com/passport/login?source=movie",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
    },
    'QQ阅读': {
        'api': 'https://ptlogin.yuewen.com/userSdk/sendmsgnew',
        'headers': {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "referer": "https://passport.yuewen.com/yuewen.html?unionshow=11110&maskOpacity=50&target=top&popup=1&returnUrl=http%3A%2F%2Fbook.qq.com%2Fywlogin%2Flogined.html%3FrefererType%3DNORMAL%26http_referer%3Dhttp%253A%252F%252Fbook.qq.com%252F&appId=1450000220&areaId=1&ticket=1&tab=qq&tabshow=111&",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        }
    },
    '一起教育科技': {
        'api': 'https://ucenter.17zuoye.com/signup/tmsignsvc.api',
        'headers': {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://ucenter.17zuoye.com",
            "referer": "https://ucenter.17zuoye.com/index.vpage",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
    },
    '爱奇艺':{
        "url": 'https://www.iqiyi.com/qiyichupin/',
        'api': 'https://passport.iqiyi.com/apis/phone/secure_send_cellphone_authcode.action',
        'headers': {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "QC005=ec28ac48466c9b80f55f53fbc048303c; QC006=1pa8bmjnugqlcos7a2hahui2; QC173=0; P00004=.1602063907.6f6275e75f; QC170.sig=5QY_l_EMGEFy9_9zKtnZraEUga4; AUDIOTRACKGUIDE=1; QP0028=1; QC124=1%7C0; Hm_lvt_292c77bd6e6064e926d1d58f63241745=1602172328; QP008=1260; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A1%2C%22isOpen%22%3A0%2C%22speed%22%3A10%2C%22density%22%3A30%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%2C%22hadTip%22%3A1%2C%22hideRoleTip%22%3A1%7D; QC021=%5B%7B%22key%22%3A%22V%E5%AD%97%E4%BB%87%E6%9D%80%E9%98%9F%22%7D%2C%7B%22key%22%3A%22%E7%A0%B4%E8%8C%A7%22%7D%2C%7B%22key%22%3A%22%E4%BB%A3%E7%90%86%E8%87%AA%E5%8A%A8%E9%85%8D%E7%BD%AEpac%22%7D%2C%7B%22key%22%3A%22kali%20%E4%BB%A3%E7%90%86%22%7D%2C%7B%22key%22%3A%22kali%20%E9%9A%90%E8%97%8F%E8%BA%AB%E4%BB%BD%22%7D%2C%7B%22key%22%3A%22%E9%9A%90%E8%97%8F%E8%BA%AB%E4%BB%BD%22%7D%2C%7B%22key%22%3A%22DDOs-Attack%22%7D%2C%7B%22key%22%3A%22ddos%20%E8%B7%AF%E7%94%B1%E5%99%A8%22%7D%2C%7B%22key%22%3A%22kali%20ddos%22%7D%2C%7B%22key%22%3A%22kali%22%7D%5D; IMS=IggQABj_5ZX9BSokCiA3YjQ3ZWRmOWVkYzM2NjY3YzE4ODhmZTIzOGFjZWE0ZRAAciQKIDdiNDdlZGY5ZWRjMzY2NjdjMTg4OGZlMjM4YWNlYTRlEACCAQCKASQKIgogN2I0N2VkZjllZGMzNjY2N2MxODg4ZmUyMzhhY2VhNGU; T00404=23d28b17d17964e84afa3e8e4c094496; QC176=%7B%22state%22%3A0%2C%22ct%22%3A1607087774305%7D; QC007=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DMB6Ss6P10zbjRh2CsPzp5bJUXPZJItfc3TuU3_Yk4PJ9n_4jcQNSc6JKrXRv_shY%2526wd%253D%2526eqid%253Db5dfe18d00008e69000000065fca2f88; QC008=1602063700.1604668157.1607087774.12; nu=0; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1607087775; QC163=1; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A%22%22%7D; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1607087784; QC010=128973448; QC160=%7B%22u%22%3A%22%22%2C%22lang%22%3A%22%22%2C%22local%22%3A%7B%22name%22%3A%22%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%22%2C%22init%22%3A%22Z%22%2C%22rcode%22%3A48%2C%22acode%22%3A86%7D%7D; PCAU=0; __dfp=a1369b50fd0ac54c6e8f6f5973778e3a3a347962b7d7c4573a8a032fa07f245168@1608383777359@1607087778359",
            "Host": "passport.iqiyi.com",
            "Origin": "https://www.iqiyi.com",
            "Referer": "https://www.iqiyi.com/iframe/loginreg?ver=1&is_reg=1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        },
        "注册按钮": {'xpath': '//*[@id="widget-userregistlogin"]/div[2]/div[3]/a'},
        '框架': {'注册框架':{'xpath':'//*[@id="login_frame"]'}},
        "手机号输入框": {'xpath': '/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/input'},
        "下一步": {'xpath': '/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/a[2]'},
        "同意": {'xpath': '/html/body/div[2]/div/div[2]/div[1]/div[2]/div[2]/a[2]'},
        "读秒": {'xpath': '/html/body/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[2]/div/div[1]'},
        '验证码': {'xpath': '//*[@id="regSlidePiccode"]/div/div/div[1]/div[2]/div/canvas'},
    },
    "中国建设银行": {
        "api": "https://sinfo.ccb.com/tran/WCCMainPlatV5",
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "WCCTC=28631138_1468485748_648936104; FAVOR=|||||||||0|; tranCCBIBS1=KG5n5%2CEMwVq6Z63sw8ajkZFdgXXGU6FJgmnJ4JFchw3hV5phmqXmcVNysFnVYhKnglXDw9EqivnzgtG1hSH2wxGmitXH4yTWCC5cJe; ccbcustomid=341bdc47b6903393uwNTEbEmOAvjjCKYpHF316065616276224NkRfhnD2UPuwgRCPHTuc3866188dbbddf7b23a8c8d230f199c6; cityName=%E5%8C%97%E4%BA%AC%E5%B8%82; cityCode=110000; bankName=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%88%86%E8%A1%8C; bankCode=110000000; cityCodeFlag=2; cityCodeCustId=; ccbsessionid=RbtTBOBItGf0E8k90f2bcaeb0d8-20201204222359; ticket=; cs_cid=; custName=; userType=; lastLoginTime=; JSESSIONID=LZ0uJ0u-1WuufhWjYoVg81-oKdCEODO8OayoakDYeNlGIkKgdCk3!753460155; null=925041418.20480.0000; cookieidTagFlag=1; tagInfoId=%26_000094%3D1%26_000050%3D12; lastUpdateTime=2020-12-04%2022%3A24%3A36; tranFAVOR=HeRWmCwrFsrQ7bjHNrY97pjTNvYR7xjDN2YY7yjxN4YN7fjENJYO7qcObgbi84OpXeQZjj; INFO=8j9f|X8pMJ",
            "Host": "sinfo.ccb.com",
            "Origin": "https://sinfo.ccb.com",
            "Referer": "https://sinfo.ccb.com/tran/WCCMainB1L1?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainB1L1&TXCODE=NHY015&SOURCEFLAG=&tourl=http://member.ccb.com/cn/mycom/user_center.html",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        },
    },
    "阅文集团": {
        'url': 'https://passport.yuewen.com/reg.html',
        '手机号输入框': {'xpath': '//*[@id="txtphonenumber"]'},
        '发送验证码按钮': {'xpath': '//*[@id="get_code"]'},
        '滑块': {'xpath': '//*[@id="tcaptcha_drag_thumb"]'},
        "框架": {'拼图框架':{'xpath': '//*[@id="tcaptcha_iframe"]'},}
    },
    "淘宝网": {
        'api': 'https://reg.taobao.com/member/checkcode/mobile_validation_choice.do?type=NormalRegistrationV2',
        'headers': {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "t=752935e5f5e49de0dbfec07ed93672f7; cna=BJoDGIc5/hUCAXjvkjZXWQCC; miid=867173341552671373; cookie2=138badd505af9b3a215860e29b8666b3; v=0; _tb_token_=537317db7e419; xlly_s=1; regsid=277e40d60c2722068f57b08a4cf96e171825df7f; regsc=6364291641d97bd89b1a5f63da96cdfd04bb06511c70ddf7319625a491d4ac7c; regtraceid=f4f73a662fc4729bd022e557f192e45c; tfstk=cquRBdg_sKvkK1Nx_0KcAmKCXUAcahb8p_wNJCkeEZi2aZQdRsfSSVFoa3NOerdA.; l=eBg5oQ_7Oe3Vmy_XBO5Zlurza779zIOfC1PzaNbMiInca6GP9FwuENQ2_Gt9Wdtjgt5c3Etrb3kJjREyWxz38x6TIcZseKnG43vw7e1..; isg=BHl5FQzTAqKkT942aB-pQviliOVThm04ALaSBJuvoKAfIpy079TkCZM0oCbUnQVw",
            "origin": "https://reg.taobao.com",
            "referer": "https://reg.taobao.com/member/reg/fill_mobile.htm",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
    },
    "央视网": {
        'api': 'https://reg.cctv.com/openapi/v2/user/verification/sms/code?timestamp=1607100492',
        'headers':{
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "cna=FVdRGC3V5n0CAXjvknL7/itR; sca=0c7fa5f9; atpsida=180adc3c1a4703d19a36b729_1607100701_1",
            "Host": "reg.cctv.com",
            "Origin": "https://reg.cctv.com",
            "Referer": "https://reg.cctv.com/regist.html?from=http%3A%2F%2Fydcm.cntv.cn&backurl=http%3A%2F%2Fydcm.cntv.cn%2Fnew%2Findex.shtml",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        }
    },
    "列表网": {
        'url': 'http://www.liebiao.com/register/',
        'api': {
            '短信验证码':'http://www.liebiao.com/register/phcaptcha',
            },
        'headers': {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "_uv_id=168571508915963627; insert_cityandcate_record=1%2C1201; cities_last_visited=1; Hm_lvt_d1c8e5c1164dcc070ae572bcabfe773f=1607101378; _referid=0; id_t=3179774688%2C1607101616; _csrf=-MvxqdM4HA0VUVO6QOK8HHz01XnhYUuT; _z=bm6icbi05g7c2rhb2ooqp88eh3; Hm_lpvt_d1c8e5c1164dcc070ae572bcabfe773f=1607101380",
            "Host": "www.liebiao.com",
            "Origin": "http://www.liebiao.com",
            "Referer": "http://www.liebiao.com/register/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        },
        "手机号输入框": {'xpath': '//*[@id="phonenum"]'},
        '密码输入框': {'xpath': '//*[@id="phpassword"]'},
        '验证码输入框': {'xpath': '//*[@id="captcha"]'},
        '发送验证码按钮': {'xpath': '//*[@id="getCaptcha"]'},
        '验证码': {'xpath': '//*[@id="captchaImg"]'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\liebiao.png'}
    },
    "MobTech": {
        'url': r'https://www.mob.com/developer/register?back=%2FmobService%2Fmobpush%3Fsource%3DindexBanner',
        'api': {'短信验证码':'https://api.os.mob.com/api/verification/code'},
        '手机号输入框': {'xpath': '//*[@id="app"]/section/div/div[2]/div[2]/section/div[3]/div[1]/form/div[1]/div/div[2]/input'},
        '验证码输入框': {'xpath': '//*[@id="app"]/section/div/div[2]/div[2]/section/div[3]/div[1]/form/div[2]/div/div[1]/input'},
        '验证码': {'xpath': '//*[@id="app"]/section/div/div[2]/div[2]/section/div[3]/div[1]/form/div[2]/div/div[2]/img'},
        '发送验证码按钮': {'xpath': '//*[@id="app"]/section/div/div[2]/div[2]/section/div[3]/div[1]/form/div[3]/div/button/span'},
        "headers": {
            "Host": "api.os.mob.com",
            "Origin": "https://www.mob.com",
            "Referer": r"https://www.mob.com/developer/register?back=%2FmobService%2Fmobpush%3Fsource%3DindexBanner",
        },
        'path': {'验证码': str(sys.path[0]) + '\\code\\MobTech.png'}
    },
    "_19lou":{
        'api': {'短信验证码': 'https://wenzhou.19lou.com/util/capture/register/mobile'},
        "headers": {
            "Cookie": 'JSESSIONID=9EFA73F9699F296829212AC681BB3EE0; reg_referer="https://www.baidu.com/link?url=KTs8dusTxprQ-czGfc4YwyMl_qv0-VwfUT3meiGeUBfwBW7LHnfxW7Yf-psZ03QQ&wd=&eqid=d04c96d30009b685000000065fcb26d0"; f100big=yw147; UM_distinctid=176318c0ffd36d-04685d126039c1-4353760-e1000-176318c0ffe23d; CNZZDATA1273801387=1641870889-1607149196-https%253A%252F%252Fwww.baidu.com%252F%7C1607149196; _DM_SID_=c6570b29fbc44d9f7b89a5ea5c72b889; _DM_S_=cd1f0dc3104324033e0a1db319182890; reg_source=baidu.com; reg_step=1; reg_kw=; reg_first=https%253A//wenzhou.19lou.com/register; Hm_lvt_14b9477f0f22097acc750bf905bf965c=1607149033; Hm_lpvt_14b9477f0f22097acc750bf905bf965c=1607149033; fr_adv=; _9755xjdesxxd_=32; __snaker__captcha=s2OABC80Bn5HLIpy; gdxidpyhxdE=BE6cYH2RQZyL%2FVPprvj4ZQyHe%2Bup2NQEb5Pyw9OeyuoNVlnt9srUaQtcAnskccxbstWzSI8tYjQiHG%5CI5nyxRL7gPZ0WjSYazOJX9Zp%2FJLyjlaVP8WWwGcfvY3D3s4n6OUfqXr%2FCbKdUd8ut%2Fk6%5Cro%2BAWCoTm6t2aPHo%2FTCJI%2FKLmj%2Fi%3A1607150791669; fr_adv_last=captcha_Netease_mobileCode_0',
            "Host": "wenzhou.19lou.com",
            "Referer": "https://wenzhou.19lou.com/register",
        },
    },
    "金数据": {
        'api': {'短信验证码':'https://jinshuju.net/signup/sms_code_confirm'},
        'headers': {
            "cookie": "_smt_uid=5fc24980.362cdddd; _help2_session=RjF2a0JHdkRpNmczWURYQVV1NzBLQjRPcFVpUG9EbXdwRjYvTmdaTmJMUi91Y282Nm5tS2ZPSTMzQmdicEdab1F1RmRmWHFMbkMzVXBvd01CYml5UEE9PS0taEdia3ZZTW9RWmQrRCszV0dGUFZGUT09--28783795cda45d1d92f97c891e196742ea3f0891; jsj_uid=6591bdc7-91ca-49c4-9d19-c8a4c4f2a972; referer_url=https%3A%2F%2Fjinshuju.net%2Fhelp%2Farticles%2Fregister-login; Hm_lvt_47cd03e974df6869353431fe4f4d6b2f=1607151537; _ga=GA1.2.1192073687.1607151556; _gid=GA1.2.486406236.1607151556; _gd_session=bzdEWlFTdTVaYlcwUFl3OWNNZjRlOVJMajhidzR5blExS0tqajFMNHA4V3UzdGZNR2VFZ2hOL1pjZHU2NXNHNC9Yb2ZyZlVjMnhkck53TExZczB1WmRHRWY0LzJvSmdxNUtoNGV1ZjZIdjlOeWd3VjgzZ1I5bGxmbGhFaDRFdExadTRDWDBlanB4Wm9DaHQyMFg2ZVBRL1RJRnhlYjZ5bEdZblQ0blpqQ2RyamhuVnZOOGI2c0ZiRVVuTkx5bC83WFhIOGs3QjF1VStyOURWQXpKeThWSGVYdDd2ZCtjQjFxZnFaN015eVdWcXhoeTZrL2ZiSHYzVjZqQnFtY1NkRHZ0TGlQV2xJVGZJaG5CcytrQ3pIU1JWam8wYkdvL2IxOEJGMjh2UU82M2RsSThNV0hHaFR5dmVNYnVzSDNTM05PaG4rYVFKV1RiK1A5c1BYTDJ4bHVpRndHMU92UzQvWDliYmIvOVNQU1hnPS0tZGh1bGszWDRUazhRb3dYY1RqZmQxdz09--352ef76ef0b5c25617b27a735ec1337d670a1eb3; Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f=1607151564",
            "origin": "https://jinshuju.net",
            "referer": "https://jinshuju.net/signup/sms_code_confirm/new",
            "x-csrf-token": "Mq4LeU9sgo2f8oeAIryAVSgfBJh/Xh7JesgMIdUY3JJd0mg7dh71eMM+QtcREm6FCIE6tgtx4vQwH/m6n50EDw=="
        }
    },
    "江苏政务服务": {
        'api': {
            '短信验证码': 'http://www.jszwfw.gov.cn/jsjis/front/register/sendmobilerand.do',
        },
        'url': 'http://www.jszwfw.gov.cn/jsjis/front/register/perregister.do',
        "headers": {
            "Cookie": "_pubk=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC%2FM868kojjC5nTlW2VAXw%0AWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh%2FYqtv8eTpRQq6TCMyaU8u%2Fvj5rZsqFR7wEOEL%2BzDdt7Xr%0A%2Fn7aoOwRDMYRPdnxV5PwyDLYrVGX4%2Fx4%2BSxcpbflgchjPHx10ubEd7KM2QIDAQAB%0A; pageUrl=http%3A%2F%2Fwww.jszwfw.gov.cn%2Fjsjis%2Ffront%2Fregister%2Fperregister.do; JSESSIONID=01FE6A2EFAF6DAAECFC0195A9CBA11C1; acw_tc=b7f0b29d16077974216824937ec78ca70ed49d57b6b94f58918d2296d5;",
            "Host": "www.jszwfw.gov.cn",
            "Origin": "http://www.jszwfw.gov.cn",
            "Referer": "http://www.jszwfw.gov.cn/jsjis/front/register/perregister.do",
        }
    },
    "中国网球协会会员网": {
        "url": 'http://www.imcta.cn/zhuce_gerenhuiyuan_userzhuce.jsp',
        "api": {'短信验证码': "http://www.imcta.cn/console/pub/yanzhengma/yanzhengma_save_www.jsp?handle=getMobleYanzhengma"},
        "headers": {
            "Cookie": "JSESSIONID=AD0FE03E8BCC3F7FBC69382C98E14674; JSESSIONID=22012DA1C438D59DA0C63EB7A9885A5C",
            "Host": "www.imcta.cn",
            "Origin": "http://www.imcta.cn",
            "Referer": "http://www.imcta.cn/zhuce_gerenhuiyuan_userzhuce.jsp",
        },
        'path': {'验证码': str(sys.path[0]) + '\\code\\imcta.png'},
        '验证码': {'xpath': '//*[@id="randImage"]'}
    },
    "广东学习网": {
        'api': {
            '短信验证码':'http://www.gdsjxjy.com/com/sendSmsCaptcha',
            '图片验证码': 'http://www.gdsjxjy.com/com/checkImgCaptcha',
            },
        "headers": {
            "Cookie": "edu-s=c78486dd6026471bb2935f05c5416190; UM_distinctid=17636246d5e3c0-02729140d82ade-4353760-e1000-17636246d5f42; CNZZDATA1000522201=1130698882-1607225241-null%7C1607225241; Hm_lvt_fdb4553cfc73802c294f0c278bb416fe=1607226126; Hm_lpvt_fdb4553cfc73802c294f0c278bb416fe=1607226126",
            "Host": "www.gdsjxjy.com",
            "Referer": "http://www.gdsjxjy.com/user/register",
        }
    },
    "起跑运动": {
        'api': {'短信验证码': "http://app.35191133.cn/api/mobile/power/sendcode"},
        "headers": {
            "Cookie": "newapp=1; isProductLocking=1; isNewsLocking=1; foot={%22id%22:%22373%22%2C%22cate%22:%22footer%22%2C%22title%22:%22%E9%A6%96%E9%A1%B5%22%2C%22piclink%22:%22shop-o%22%2C%22links%22:%22/shop/buyers%22%2C%22show%22:%221%22%2C%22desc%22:%22%E6%9C%8B%E5%8F%8B%E5%9C%88%22%2C%22sort%22:%225%22}",
            "extra": '',
            "Host": "app.35191133.cn",
            "meid": '',
            "Origin": "http://app.35191133.cn",
            "Referer": "http://app.35191133.cn/login?VNK=1887b37b",
            "timestamp": "1607231955",
            "uid": ''
        },
    },
    "多点": {
        'api': {'短信验证码': 'https://gatewx.dmall.com/user/sms'},
        'headers': {
            "Cookie": "tempid=C929FC6183000002BD2D597013B812B8; session_id=C929FC6183200002BB966FCC14309A00; updateTime=1607241775260; inited=true; first_session_time=1607241777679; web_session_count=1; pos_get_time=1607241778840; wxLocName=%u77F3%u5357%u5357%u8DEF12%u53F7%20%u946B%u6E90%u8C6A%u5EAD; wxLoc=110.282119%2C21.590199; wxHitStore=%7B%22bizType%22%3A1%2C%22brandId%22%3A0%2C%22storeId%22%3A108611%2C%22venderId%22%3A5881%7D; wxIsUpdateConsign=false; storeGroup=1-108611-5881; data_seq=9",
            "Host": "gatewx.dmall.com",
            "Origin": "http://i.dmall.com",
            "Referer": "http://i.dmall.com/",
        }
    },
    "拼多多": {
        "url": 'https://mobile.yangkeduo.com/login.html',
        'api': {'短信验证码': 'https://mobile.yangkeduo.com/proxy/api/api/sigerus/mobile/code/request?pdduid=0'},
        "headers": {
            "cookie": "api_uid=CkkLR1/N1DV+qQBZf/hMAg==; _nano_fp=XpEonqXxn0TbX5T8no_RecZ3wcSI1wlboO0dyM7f; webp=1; pdd_vds=gadLxIwiLPbidLtnsIOytLGodQEimQnmIEbynNLELibmxNyylGdatGwNLbGQ",      
            "origin": "https://mobile.yangkeduo.com",
            "referer": r"https://mobile.yangkeduo.com/login.html?from=https%3A%2F%2Fmobile.yangkeduo.com%2Fpersonal.html%3Frefer_page_name%3Dindex%26refer_page_id%3D10002_1607324492265_deoncusynv%26refer_page_sn%3D10002&refer_page_name=personal&refer_page_id=10001_1607324496377_i7ggooo789&refer_page_sn=10001",
        },
        "手机登录": {'xpath': '//*[@id="first"]/div[2]/div/span'},
        "手机号输入框": {'xpath': '//*[@id="user-mobile"]'},
        "发送验证码按钮": {'xpath': '//*[@id="code-button"]'},
    },
    "火箭交易所": {
        'url': 'https://fxxx.fx-dd.com/wap/#/register',
        'api': {
            '短信验证码': 'https://fxxx.fx-dd.com/api/v1/user/verify/GetSmsVerify',
            '图片验证码': 'https://fxxx.fx-dd.com/captcha.html?id=0.38073782264228306',
            },
        'headers': {
            "Cookie": "lang_set=zh-cn; SESSION=9cjo42vhi7aqbe1ftvamifr9nd",
            "Host": "fxxx.fx-dd.com",
            "Origin": "https://fxxx.fx-dd.com",
            "Referer": "https://fxxx.fx-dd.com/wap/",
        },
        '验证码': {'xpath': '//*[@id="captcha-msg"]/div[3]/div/img'},
        "手机号输入框": {'xpath': '//*[@id="app"]/div/div[1]/div[3]/div[1]/div/div[5]/div[2]/input'},
        '验证码输入框': {'xpath': '//*[@id="captcha-msg"]/div[2]/input'},
        '发送验证码按钮': {'xpath': '//*[@id="app"]/div/div[1]/div[3]/div[1]/div/div[7]/div[2]/div[3]/div'},
        'path': {'验证码': str(sys.path[0]) + '\\code\\rocket.png'}
    },
    "互亿无线": {
        'url': 'https://user.ihuyi.com/register.html',
        'api': {'短信验证码':'https://user.ihuyi.com/api/reg_sendsms.php'},
        "headers": {
            "Cookie": r"geturl=s%3Dbaidu%26m%3Dcpc%26k%3D58114%26renqun_youhua%3D1960122%26bd_vid%3D11374836253357125026; Hm_lvt_a7cb923517914c42fc2295e413b6756b=1607341174; Hm_lpvt_a7cb923517914c42fc2295e413b6756b=1607341174; acw_tc=2f624a4816073414398007617e11e4e270ae93a4ca41a7b3333ff9770b459a; PHPSESSID=kndruonolcdmh7h89hcqcvghd6",
            "Host": "user.ihuyi.com",
            "Origin": "https://www.ihuyi.com",
            "Referer": "https://www.ihuyi.com/sms.html?s=baidu&m=cpc&k=58114&renqun_youhua=1960122&bd_vid=11374836253357125026",
        },
        "滑块": {'xpath': '//*[@id="nc_1_n1z"]'},
        '手机号输入框': {'xpath': '//*[@id="tel"]'},
        '发送验证码按钮': {'xpath': '//*[@id="gca"]/a'}
    },
    "年度十大司机评选": {
        'api': {'短信验证码':r'https://epassport.diditaxi.com.cn/passport/login/v5/codeMT?wsgsig=dd03-jEnsB%2B%2FuttbuNLdrTgn354VphDixKZVWScugIuOOhDiwNxaoyncC6KrZqjbwNL1UQjyN74rp%2FftRM2InTCX0HyVYrWGxNZ5wviX48NOSkttT4w9spntF8Nxx'},
        "headers": {
            "Host": "epassport.diditaxi.com.cn",
            "Origin": "http://page.udache.com",
            "Referer": "http://page.udache.com/driver-biz/driver-day/index.html",
        },
    },
    "imBC": {
        'api': {
            '短信验证码': 'https://www.bitscash.global/app/sms/registSmsCode',
            '图片验证码': 'https://www.bitscash.global/app/code/regCode',
        },
        'headers': {
            "Cookie": "JSESSIONID=DD85FA8623F4B52EE52E58BB677D3F4E; 133916___170200_KS_133916___170200=9f7c452925774fee94a00429438c8112; 133916___170200_KS_ri_ses=837397571%7C0589867EA70E5CF156C1036129CB278E-null; 133916___170200_curPageNum=1; token=; Language=zh_CN; 133916___170200_curRanId=1607499451693_1607499387574; 133916___170200_curPage_1607499387574=1_true_1607499451694",
            "csrfToken": "f7fa809fd1ea4b60a3e25538f7a19504",
            "Host": "www.bitscash.global",
            "Origin": "https://www.bitscash.global",
            "Referer": "https://www.bitscash.global/",
        },
        'path': {'验证码': str(sys.path[0]) + '\\code\\imBC.png'}
    },
    "裕农通": {
        'api': {'短信验证码': 'https://rris.ccb.com/rris/app/auth/prvt/smsCode'},
        "headers": {
            "areaCode": "440802000000",
            "businessId": "RRIS",
            "channel": "70650172",
            "Cookie": "ccbcustomid=341bdc47b6903393uwNTEbEmOAvjjCKYpHF316065616276224NkRfhnD2UPuwgRCPHTuc3866188dbbddf7b23a8c8d230f199c6; cityName=%E5%8C%97%E4%BA%AC%E5%B8%82; cityCode=110000; bankName=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%88%86%E8%A1%8C; bankCode=110000000; cityCodeCustId=; cityCodeFlag=2; ccbsessionid=RbtTBOBItGf0E8k90f2bcaeb0d8-20201204222359; ticket=; cs_cid=; custName=; userType=; lastLoginTime=; cookieidTagFlag=1; tagInfoId=%26_000094%3D1%26_000050%3D12; lastUpdateTime=2020-12-04%2022%3A24%3A36; tranFAVOR=QaBgqH4CXGv1KdRHsSX1ed6H8SF1QdBHVSY15dpHvSk1ndeHxSr1zWGVJVV%2ChtKwem",
            "DEVICE_TYPE": "other",
            "deviceNo":'',
            "Host": "rris.ccb.com",
            "Origin": "https://rris.ccb.com",
            "position": "110.36506726,21.2574631",
            "positionCode": "440802000000",
            "Referer": "https://rris.ccb.com/app/",
            "System_Id": "RRIS",
            "userId": '',
        },
    },
    "泰康在线": {
        'api': {'短信验证码':'https://xhb.bxlsj.com/mall/phone/sendVerifyCode'},
        'headers': {
            "origin": "http://xhb.axinsur.com",
            "referer": "http://xhb.axinsur.com/ax-product-zjStandard?",
        }
    },
    #固定请求头(通用)
    "headers": {
        #接收什么类型数据
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, application/json, text/plain, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",#接受编码
        "Accept-Language": "zh-CN,zh;q=0.9", #接受语言
        "Connection": "keep-alive", #连接保持链接
        #提交json用 "application/json; charset=UTF-8"
        #提交表单用："application/x-www-form-urlencoded; charset=UTF-8"
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", #内容类型
        #表示请求的目的地，即如何使用获取的数据；
        "Sec-Fetch-Dest": "empty",
        #请求的模式:跨域请求；
        "Sec-Fetch-Mode": "cors",
        # 表示一个请求发起者的来源与目标资源来源之间的关系；
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        #xhr
        "X-Requested-With": "XMLHttpRequest",
    },
    # '手机号': str(input('请输入轰炸的手机号：')),
    'msg': ['该手机号已经注册', '重新', '短信发送间隔时间太短', '验证码错误','成功','succeed','发送验证码','success'],
    "时间戳键名": ["salt","ts","t","_","xajaxr","nocache"],
    "验证码键名":  {
        "验证码id":"regCodeUid",
        "图片验证码":[
            "randCode","check_code","imgMobileCaptcha","regCode","captchaCode",
            "inputUserId","number"
        ],
        "验证条":"sig"
    },
    "手机号键名": [
        "tel",'mobile',"phone","identity[mobile_no]",
        "info","cell","target","PhoneNumber","mobileno","account","moveTelNo"
    ]
}


if __name__ == "__main__":
    print({"变量":"data","网站数量":len(data) - 5,"系统分配空间的大小": str(round(data.__sizeof__() /1024,2)) + ' KB'})
    headers_str = '''
phone: 13265547087
openId: 
channel: 
tags: 
chKeyName: 
chKeyValue: 
productCode: TKCN_ZJ_ZENGX_AX
'''
    print(add_yinhao(headers_str,1))