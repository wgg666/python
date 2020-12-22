# -*- encoding: utf-8 -*-
'''
@文件    :查询姓名.py
@说明    :
@时间    :2020/12/17 20:31:08
@作者    :AwAit
@版本    :1.0
'''

import requests
import time
api = 'https://shenghuo.alipay.com/transfer/getUserInfo.json'
#https://authet2.alipay.com/login/index.htm
headers = {
    "accept": "text/javascript, text/html, application/xml, text/xml, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": 'JSESSIONID=271CA35B8556A737A09E38FC05C308FA; csrfToken=fxKAxoA0FQphJxHOMpeL0Qto; mobileSendTime=-1; credibleMobileSendTime=-1; ctuMobileSendTime=-1; riskMobileBankSendTime=-1; riskMobileAccoutSendTime=-1; riskMobileCreditSendTime=-1; riskCredibleMobileSendTime=-1; riskOriginalAccountMobileSendTime=-1; cna=sL5gGInrvjkCAXjvkjIhDVAw; session.cookieNameId=ALIPAYJSESSIONID; UM_distinctid=176709bf9a5156-0d717bd2dcc14f-c791039-e1000-176709bf9a625e; _uab_collina=160829335601853159910513; _umdata=GF20C3BB9944691001AA8AC499C30F4253EA513; unicard1.vm="K1iSL19gs+tqoJlZ7ssTew=="; JSESSIONID=271CA35B8556A737A09E38FC05C308FA; spanner=9U9pKJjRunmL+SHEFuDCoJB2Il54pYjD4EJoL7C0n0A=; ctoken=cTJe8SwDZXUtz_Ur; umt=Lc4751f9bfbe9c331ac6c1600869d1322; ALIPAYJSESSIONID=RZ42psYhdrhuRqiyqb2cvCJR2EfzuXauthGZ00RZ42; zone=RZ42A; rtk=C3nv5IcjQdnILWD6M3U2ldGoi+YlxedZotakXl+E8asHiPrPOYh',
    "origin": "https://shenghuo.alipay.com",
    "referer": "https://shenghuo.alipay.com/send/payment/fill.htm?_pdType=afcabecbafgggffdhjch&_tosheet=true",
    "sec-ch-ua": 'Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}
timeSnap = str(int(time.time() * 1000))
data = {
    "timeSnap": timeSnap,
    "ua": "w9ur_Kk2.WfctxUvLudJXp3FKzjis1Zq.NK1D29yyqrH65F.CYFl86mJMbgIhHVDn3yZv_28IDIEK_IC99AGtrB2qPQ14ROEL.rh2dlb6OAgdjKTSQ3czBltShEERC4nxd4bm8hp.KuzqRFjCi5Diutw96WQkutg67OfvCtocJ0S_HjQxpkc2cPXQ6AukOSgY2Xhh0Z.aG0ebqWVf87OWCXnnTPfzuXkmPxLNJiXqOU4gm4lMQbeXjlOzK0Z1Ct7GGzUMNMoEj2FbsAPTGyUAyPgSypbkt4RUOO_2KKPlxlDIyDlpzopoASD81QUdk41uPuwu83MkDORYXtiM2VlYDIo5nWC5xIEtwPbKiMkFQlhPgafzG4U8gsUMvIIqAbdO29eeD7N68.mQz3tjvVP7WgWqTGvRsoPbzHpBltt.hToNbOOhWHi3EdsDDG6SXOS_GsyucVjPCyQZUNihzXWtBmN.hm0qQBow.tGNTiZ2PdirDLFrBzA6vLritowNXyVMtQwJxkH_yCEZuugmw2szVDR0j9GSJVirXq9box4rpwq9VsDybCWAWp52C1wIBvMYAt2LVNH3js4orGHsVgSP7uzx7eg7ylodY6eN_KXILFkL0996zVi6frsQZs9ACU4VkEP2Lx.QAwYNhz6jupK9fmnaytFXHuXEe0eCmM4WaMn0YJDfkVuIdOgn1c_24WKlcYXUN7J_4j0q8a0lPEOg1Kd1gZV4x.vu_EZK82XRsN9Pw6jWraI5gXZreG3LiEAzo.r39X1bfNX.aA68Y4zKR6T7kpmN6e1YPz2BvP_KqTLYj9f.YbJYo7sX0ZbsvnfFJfdU8CJDVAezw8siIhC03jhbbm6Fl8lRp9fgJaKfF.H7QE4A9WanvQd_EGOG4ZSUmiBarFFDauSIicVKbF2x2eRJwc_2RWyyU6STm3wr7mlA1OgBo77x5f32bx1JUsb_OscfrB9tZbcI6T2BSHEeK2D1UvGnSEzU_jjrjIX2R45d0AR4Hd1.FqyRaBQOhAAI9tOhGRTAyDC9X66ZdR7Ts6GqXddkxlWE0mtaTaFPaXA1851oTbiu_groUt.85.PNt9mllIEuMIq5UBFmzFYlTlLo1neFyoyEyHWN5DBj4tVuELaZzJOIVhv.Jba3VkUTFAneRr.XSsI17J3S_.76cG7e.V1oTFHEiH9hsr7N0Jt3UxP3h5XkwbbqaNyAwooU.4z2aYfnakKLSSygN7s0iWyn6LArIVq82p9P5HWScn2rpnfHWtC.AT4RPY82JWhhqMs7UEHbD.lTa5s_J3710686bv1q.i.4ZMBbJisqB5t333QAiMcbNHWqjjf1V5Ni7DSL38P.X0gTY48951woNldPAnf61dM7F144ivKqZ.MQmx78bfksJ89gvO7AN97__cJjPoxcf4YfbqHtShJhFPaNVXGZczAb_7BET5PUZH2SybFnbV7hzkdUH_Mibd72yXkWD99uZlKV_K.Y.zI2QegHyX4DeXnc6fpHhqeNXm5mZgtS7MRX6K8kucPk4iZXo28dTDJkQ8EA_LtlGdhs.mH7XoUlvCTIQNQAifwMxWkqeUYcCDfUf4WlnXWy1EeudTC5fxn768gu9I3uuINUvPDg3rPjAp4A78eBdFb8AfJOtl5okuOnCEn8SoIS7nc8eZFlezL3YIs.tyU.JGfj0tO8IGYO_sfU4Zaa2RdnKTZQi9M3QW7H4XAHzcAW.FgbKCNIbpSLgDyVn6fNjUafqpuBof0ir37eITCsOrOaTVMnvO8RV.XnmrE8GQawoGzcixMD3guW2T5fUnvfvOV5d9cO9gB_Iq0MCByBqJlQvNS2P1BgNTAubg7lVtm_r6oxaTziTCj4htX.ejw53l.LhtvCHZO97XUgXCIRA2a9W2N9SmYFfF5wo4QN9AKg9SCiQEIT6NmviuIfa29LEfVyz3y.lLvyWBT6HJ9pQtrKfsF0M1FdXh06LTZL6XCCR1DxPqLKvQW9.J4XJEwowM72Ij4X7CZ48YDhsCenfqWmCw8AwdlcPlHL1HuL5CfUT3XK52NFqEpyQiyPeRjRwxCcEzHAfo_sqjYmdK5WT7yOZRU6Tij6iLjBlzbWNV1AhlnqrFNQmcTHFFJiRXObZ91vArWN_s6haKdpwEtsf5GPx.U6bWcxTr0oy9QmqCvKRKrpdz_gX4M9c1Cjg6uaCkTTKE8OjYLlo7vlAUD81DFyR_dGCkutI6QaJvt5eueO8dgBR52E4nmmuEMgx10D_O5gYQlKpiRWE65zTvfUHAgWid",
    "rdsToken": "ppjFIGbnQKMp46zRyahVfAVRiak8Un3m",
    "account": input('查询的手机号：'),
    "userId": "",
    "_input_charset": "utf-8",
    "ctoken": "zkRUrf_Q4W9u29CC",
}

response = requests.post(url=api, data=data, headers=headers)
#["userInfo"]['name']
Userinfo = response.json()
if '账户不存在，或对方关闭了隐私开关' in Userinfo:
    print('账户不存在，或对方关闭了隐私开关')
elif '你的操作过于频繁，请稍后再试' in Userinfo:
    print(Userinfo)
else:
    #{'name': Userinfo["userInfo"]['name']}
    print(Userinfo)