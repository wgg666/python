# coding=gbk
# pip install shadowsocks
# sslocal -h显示帮助 -k密码 -m加密方式
# sslocal -s 192.168.100.3 -p 8888 -m aes-256-cfb
# ssserver --help
#Path变量里（我就忘了）。
# C:\Python34\;C:\Python34\Scripts\
#安装 OpenSSL（https://slproweb.com/products/Win32OpenSSL.html），一样，如果你装的Python是32bit的就下载32bit的版本，我是用64bit的。别忘了还需要Microsoft Visual C ++ 2008的支持库
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
# 然后保存在C：\ Python34 \ Scripts \ config.json。执行以下命令运行：
#
# ssserver -c D:\Python\Python38-32\Scripts\config.json
# 如果它报错
# >异常：找不到libcrypto（OpenSSL）
#
# 就去OpenSSL的安装目录复制libeay32.dll，libssl32.dll，ssleay32.dll到C：\ Python34 \ Scripts \
#
# 可以看到我的服务已经启动成功了！好了占用Windows下的Shadowsocks服务器吧！
'''
pip install shadowsocks-sdk
'''

