import zipfile,random,time,sys
class MyIterator():
    # 单位字符
    letters = '123'
    # 最小值
    min_digits = 0
    # 最大值
    max_digits = 0
    def __init__(self,min_digits,max_digits): 
        if min_digits < max_digits:
            self.min_digits = min_digits
            self.max_digits = max_digits
        else:
            self.min_digits = max_digits
            self.max_digits = min_digits
        
    # 迭代器
    def __iter__(self):
        return self
    # 生成器
    def __next__(self):
        rst = str()
        # randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
        for item in range(0,random.randrange(self.min_digits,self.max_digits + 1)):
            # 012345随机选一个
            rst += random.choice(MyIterator.letters)
        return rst
    
# 解压函数
def exteact():
    start_time = time.time()
    zfile = zipfile.ZipFile('.\\破解\\zip\\1.zip')
    for p in MyIterator(5,6):
        print(p)
        try:
            # 解压
            zfile.extractall(path='.\\破解\\zip',pwd=str(p).encode('utf-8'))
            print('这是密码：{}'.format(p))
            # 结束的时间
            now_time = time.time()
            print('用时{}'.format(now_time - start_time))
            sys.exit(0)
        except Exception as e:
            pass
exteact()           
