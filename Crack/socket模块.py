from socket import *


tgtHost = input('请输入你要访问的主机：')
# tgtPort = int(input('请输入你要访问的端口：'))
c_sock = socket(AF_INET,SOCK_STREAM)
""" 
TCP:SOCK_STREAM
UDP:SOCK_DGRAM
 """
tgtPorts = range(1,65536)
setdefaulttimeout(1) #超时1秒
for tgtPort in tgtPorts:
    try:
        c_sock.connect((tgtHost,tgtPort))
        c_sock.send('123'.encode())
        res = c_sock.recv(100)
        print('[+]Port：',tgtPort)
        print('[+]Proto:',res.decode())
    except:
        print('[-]Prot：',tgtPort)
        continue