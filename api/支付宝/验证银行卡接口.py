# -*- encoding: utf-8 -*-
'''
@文件    :验证银行卡接口.py
@说明    :
@时间    :2020/12/17 21:02:33
@作者    :AwAit
@版本    :1.0
'''

import requests
import time

api = 'https://finsignweb.alipay.com/api/sign_view_anon'
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",   
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": 'csrfToken=fxKAxoA0FQphJxHOMpeL0Qto; mobileSendTime=-1; credibleMobileSendTime=-1; ctuMobileSendTime=-1; riskMobileBankSendTime=-1; riskMobileAccoutSendTime=-1; riskMobileCreditSendTime=-1; riskCredibleMobileSendTime=-1; riskOriginalAccountMobileSendTime=-1; cna=sL5gGInrvjkCAXjvkjIhDVAw; LoginForm=alipay_login_auth; alipay="K1iSL19gs+tqoJlZ7ssTe9rkW9iRoRcwc98DjAbubA=="; CLUB_ALIPAY_COM=2088622155306154; iw.userid="K1iSL19gs+tqoJlZ7ssTew=="; ali_apache_tracktmp="uid=2088622155306154"; session.cookieNameId=ALIPAYJSESSIONID; UM_distinctid=176709bf9a5156-0d717bd2dcc14f-c791039-e1000-176709bf9a625e; ctoken=5PaUOg7LVxVoDECZ; ALIPAYJSESSIONID=GZ00Sdl1Cbaao6aXsfgD5uyFY4OF2GshenghuoRZ42GZ00; zone=GZ00D; locale=zh-cn; CHAIR_SESS=ASNU2qxKQaG_q5JvuZnwSC6ND0xLaQv_fZa9vqUDKbK0L4hiSvU3rI-A4OljKH5AciBdI6Enp-yP48LuP1Ng8OLnJtwT0QYX5vPMf6CXOfSkAqjfNujAdHtnVVIxeyYEYpGI9Kxr0jRuRqa3a_wA4NtRuOHB2WbByPq3RuSQSHhKn4MhP-5WwE9whlUCVD0_8wJ-H1jNhccWdgYUd6ImE-n5SGHh7au7GLvk_Gb2QI6k3fjuKUVZ1fVwerviSfJ6JbzyC-gzL13VRJY-_8yt77jyxgRNG0vl8uo-7sPyVAq0iD1aUFnSO3tyEuDhHWMexdRYBYGrov9oNzlC4P1nnJtERbKCqEncUnD3wDasq5cFbeDKOotrKZOM__2clfSVqqt71wenoi4T3ThtazXq1X9xWDedT7D39zx2SXsCFSG58oNxsVVuXo-5sPuUUt9eAJgiqI18dzZHxIRxlg1MYvVA7Ar2fOKRKWbetfWnGYuUzmwbQZ7xGKi6vYCQB6KMJpU6Kj3b4erxpkJgDEvuTX6v_eYDd44OwA5M3jezF6em-c1tQkxPM5hrVRAOPSEBmEniQHR3QxH-eIsSx0oHGE8BpUf--nbuhDFVMNCnHli3yO92eLjOYxvVwkyTRy3luQMEaEZHD2myZ6pM8xPb8jynBScFxp-acT9E40L_TQZMSlyx1oQ2Xwa7p7QYIvJiQhrWzhNohOKGyEWfaIMpSbQ59s6x4M9bfv3WAhyz7MyfyP1kCrGHuLEK1jWnXCovUJbTSSIk3EJkiCdOxdET32nV1S5qH3K8i-nMXNUXe3MnBlzyMK0f809_LXegp0B1H5jwZyEYnItyV5B5xB5qB8_ytiiQXQXyUBNtWUxHAVCK9G12dYb5myHSSkc-TBUGbjqQgAIlwykxrVlDb8CVUdID3bXQevSvG1WXg_koYgf97wTiyg6IwyBM08w2rYSnf0gnGN-MDrRpF-Gv3Q-c-0GiBuDdVoYnpRdi6VfTXq3N3n23PwNt7L9y5XuzBOg0EZ8hreJSjZkF9DfJeXIbGHFWleX-429VvfGcQK119PE=; spanner=x4qH6d83q09Dwi/Y2w0yo37lwojYUTQ4; rtk=8wj4/JdCkCyJzq7O/wSYucXzjoNaDW5ygV+sVMz78anjOMzt62B',
    "origin": "https://finsignweb.alipay.com",
    "referer": "https://finsignweb.alipay.com/sign/form_anon?signFrom=membercenter&signProduct=EXSC_IDENTITY_VERIFY001&sp=1-resetQueryPwd-fullpage&contextParams=IaDoNUYEY%2BqJBWLZIYdTDM%2FEFTZbyxIAkwHszlkzG8pnvtBhYM6PFIVwG4aM2d1%2F6QvkV3PN9aZeMMu1gshh9j%2FUwnr4Qxb48g37I46USyVcCBDVQZrqG89p2tTuBeOaqreCcAKsLzeC462ijZ25KMhn56oeqI1iNMXEzlwfbyGMuKG54yjQwMP1Gw9ZNeIK9nRhb3FHP8chmejp9xUtjjstfLHAwVofBBlsmsseV%2BKOizDigPNzdQtvX%2Bi%2BC50qwF7E13Fx3Bo82pGUA5nAPbZX2UVr7hfxtrbcvjmYVG47nyE%2BjdjzdJaGyewaoyPXCqLTnXPm1Pdk2oVdwv9pJg%3D%3D",
    "sec-ch-ua": 'Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

data = {
    "uniqId": "6f2713e7-d9b7-4b0b-bb95-0a5a7260ef6c",
    "cardNo[cardNo]": input('银行卡号：'),
    "_input_charset": "utf-8",
    "ctoken": "5PaUOg7LVxVoDECZ",
}
response = requests.post(url=api, data=data, headers=headers)
""" 
{'isSuccess': True, 'instId': 'PSBC', 'cardType': 'DC', 
'instAgreementTitle': '中国邮政储蓄银行储蓄卡快捷支付业务线上服务协议', 
'instAgreementUrl': 'https://cshall.alipay.com/hall/showKnowledgeInfo.htm?knowledgeId=535183', 
'signElements': ['cardNo', 'cardType', 'cardHolderName', 
'certType', 'certNo', 'mobile'], 
'signCertTypes': ['A', 'B', 'N', 'M'], 
'cardNo': '621799*********5419'}
 """
yhkinfo = response.json()
# print(yhkinfo)
print({'instId':yhkinfo['instId'],'cardType':yhkinfo['cardType'],'instAgreementTitle':yhkinfo['instAgreementTitle']})