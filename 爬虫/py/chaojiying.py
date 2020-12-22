# coding:utf-8
import requests
from hashlib import md5

print('导入了超级鹰模块！！！')
# 超级鹰客户端
class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        # 设置编码
        password = password.encode('utf8')
        # MD5加密返回16进制
        self.password = md5(password).hexdigest()
        # 软件id
        self.soft_id = soft_id
        # 基本参数
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,#验证码类型
        }
        # 插入用户名、密码、id
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        response_post = requests.post(
            'http://upload.chaojiying.net/Upload/Processing.php',
            data=params, files=files, headers=self.headers
            )
        # 返回响应信息
        return response_post.json()

    # 上传报错题目的图片ID
    def ReportError(self, im_id):
        params = {
            'id': im_id,#报错题目的图片ID
        }
        params.update(self.base_params)
        response_post = requests.post(
            'http://upload.chaojiying.net/Upload/ReportError.php', 
            data=params, headers=self.headers
            )
        return response_post.json()


if __name__ == '__main__':
    # 用户中心>>软件ID 生成一个替换 96001
    chaojiying = Chaojiying_Client('wgg666', 'XWL520886', '909792')
    local_code = '.\爬虫\code\code.jpg'
    im = open(local_code, 'rb').read()
    # 1902 验证码类型
    # print(chaojiying.PostPic(im, 1902))
    # 'pic_str'查看识别出的验证码
    # 12306验证码类型：9004
    # result = chaojiying.PostPic(im, 1902)
    # all_list = [] #存储要点击的坐标[[x1,y1],[x2,y2]]
    # if '|' in result:
    #     list_1 = result.split('|')
    #     count_1 = len(list_1)
    #     for i in range(count_1):
    #         xy_list = []
    #         x = int(list_1[i].spilt(',')[0])
    #         y = int(list_1[i].spilt(',')[1])
    #         xy_list.append(x)
    #         xy_list.append(y)
    #         all_list.append(xy_list)
    # else:
    #     x = int(result.split(',')[0])
    #     y = int(result.split(',')[1])
    #     xy_list = []
    #     xy_list.append(x)
    #     xy_list.append(y)
    #     all_list.append(xy_list)
    err_result = chaojiying.ReportError('1124815475132100164')
    print(err_result)