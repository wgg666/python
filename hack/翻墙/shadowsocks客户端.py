# coding=gbk
# pip install shadowsocks
# sslocal -h��ʾ���� -k���� -m���ܷ�ʽ
# sslocal -s 192.168.100.3 -p 8888 -m aes-256-cfb
# ssserver --help
#Path������Ҿ����ˣ���
# C:\Python34\;C:\Python34\Scripts\
#��װ OpenSSL��https://slproweb.com/products/Win32OpenSSL.html����һ���������װ��Python��32bit�ľ�����32bit�İ汾��������64bit�ġ������˻���ҪMicrosoft Visual C ++ 2008��֧�ֿ�
# C:\Program Files\OpenSSL-Win64
# {
#     "server":"0.0.0.0",
#     "server_port":8388,
#     "local_address":"127.0.0.1",
#     "local_port":1080,
#     "password":"123456",
#     "timeout":300,
#     "method":"aes-256-cfb",
#     "fast_open":false
# # }
# Ȼ�󱣴���C��\ Python34 \ Scripts \ config.json��ִ�������������У�
#
# ssserver -c D:\Python\Python38-32\Scripts\config.json
# ���������
# >�쳣���Ҳ���libcrypto��OpenSSL��
#
# ��ȥOpenSSL�İ�װĿ¼����libeay32.dll��libssl32.dll��ssleay32.dll��C��\ Python34 \ Scripts \
#
# ���Կ����ҵķ����Ѿ������ɹ��ˣ�����ռ��Windows�µ�Shadowsocks�������ɣ�
'''
pip install shadowsocks-sdk
'''

