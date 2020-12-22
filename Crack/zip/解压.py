import zipfile #导入模块，它是做压缩和解压缩的

password="123321" #我们设定的口令

zfile = zipfile.ZipFile("F:\\programming\\python\\破解\\zip\\11.zip") #要解压缩的压缩包

zfile.extractall(
    path='F:\\programming\\python\\破解\\zip\\',
 members=zfile.namelist(),
 )