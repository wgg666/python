import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5



def encrypt(text,publicKey):
    #把base64解码成二进制bytes公钥
    # public_key = base64.b64decode(publicKey)
    #导入公钥
    rsakey = RSA.importKey(publicKey)
    #实例化加密对象
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    #进行加密 
    # 把字符串编码成字节，在加密成16进制字节b'\x...'，最后编码成base64字节
    results = base64.b64encode(cipher.encrypt(text.encode(encoding='utf-8')))
    #编码成utf-8的base64字符串
    results = str(results,encoding='utf-8')
    return results

if __name__ == "__main__":
    key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC/M868kojjC5nTlW2VAXwWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh/Yqtv8eTpRQq6TCMyaU8u/vj5rZsqFR7wEOEL+zDdt7Xr/n7aoOwRDMYRPdnxV5PwyDLYrVGX4/x4+SxcpbflgchjPHx10ubEd7KM2QIDAQAB'
    publicKey = '-----BEGIN RSA PUBLIC KEY-----\n' + key + '\n-----END RSA PUBLIC KEY-----'
    result = encrypt('13265547087',publicKey)
    # print(publicKey)
    print({"加密结果":result,'长度':len(result)})
