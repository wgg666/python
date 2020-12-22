import base64
import execjs
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
with open(r'.\hack\Bombingtool\江苏政务服务\rsa_util.js',encoding='utf-8') as f:
    JsData = f.read()
    # .encode().hex()
pubk = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC/M868kojjC5nTlW2VAXwWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh/Yqtv8eTpRQq6TCMyaU8u/vj5rZsqFR7wEOEL+zDdt7Xr/n7aoOwRDMYRPdnxV5PwyDLYrVGX4/x4+SxcpbflgchjPHx10ubEd7KM2QIDAQAB'
text = execjs.compile(JsData,).call('RSAencode','13265547087',pubk)
# print(len(text),'\n',text,'\n')
print(text)
# rsa算法生成实例
