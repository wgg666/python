# coding=utf-8
import os

cmd = {
    "重启explorer": "taskkill /f /im explorer.exe && explorer.exe",
}


# 打开文件夹
def open_folder(name):
    folder = {
        "mysql": "explorer C:\phpstudy_pro\Extensions\MySQL5.7.26",
        "apache": "explorer C:\phpstudy_pro\Extensions\Apache2.4.39",
        "php": "explorer C:\phpstudy_pro\Extensions\php\php7.3.4nts",
        'hosts': "explorer C:\Windows\System32\drivers\etc\hosts",
        "python": "explorer D:\Python\Python38-32",
        "f:python": "explorer F:\programming\python",
        "f:编程": "explorer F:\programming\编程"
    }
    os.system(folder[name])


# 清理垃圾
def del_garbage():
    os.system('del /f /s /q %temp%\\*.*')


def close_port():
    os.system('netstat -anop tcp')
    port = input('请输入要查询的端口：')
    os.system(f'netstat -ano | findstr "{port}"')
    pid = input('请输入pid：')
    os.system(f'tasklist | findstr "{pid}"')
    if input(f'是否关闭{port}的进程：y/n：\n') == 'y':
        os.system(f'taskkill /pid "{pid}" /F')


if __name__ == '__main__':
    pass
    open_folder("f:python") #打开文件夹
    # close_port()  # 关闭端口
    # del_garbage()  # 清理垃圾
