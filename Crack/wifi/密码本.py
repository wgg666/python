import itertools as its

words = "0123456789"
# 生成几位密码
r = its.product(words,repeat=11)
dic = open('11位数字密码.txt','a')
for i in r:
    dic.write(''.join(i))
    dic.write(''.join('\n'))
dic.close()