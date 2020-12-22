

a = 'e10adc3949ba59abbe56e057f20f883e'

#0,2,4,6,8,...
for i in range(0,len(a),2): #1个字节对应8位2进制数=2位16进制数
    print(chr( int(a[i:i+2],16) ),end='') #两两取出转成字节; 16进制转10进制; 
    

