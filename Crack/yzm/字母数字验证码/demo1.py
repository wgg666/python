# coding=utf-8
import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess

'''
https://github.com/UB-Mannheim/tesseract/wiki
从网上找到相应的‘Tesseract-OCR’下载安装（寻找对应版本）：https://github.com/tesseract-ocr/tesseract/wiki
安装后的默认文件路径为（这里使用的是Windows版本）：C:\Program Files (x86)\Tesseract-OCR\
然后将源码中的：
tesseract_cmd = 'tesseract'
更改为：
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
再次运行之前的PY脚本，成功.
'''


def recognize_text():
    # 实现色彩空间转换 转换为灰度图
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # 使整个图像呈现出明显的黑白效果 二值化取反|提取图像最佳阈值
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 获取结构元素 变形修正
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
    # 形态变异 变形_打开
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    # 变形校正
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))
    # 形态变异 变形_打开
    open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    #打开处理后的图片
    cv.imshow("ninary-image", open_out)
    # 对图像（灰度图像或彩色图像均可）每个像素值进行二进制“非”操作
    cv.bitwise_not(open_out, open_out)
    # 实现array到image的转换
    textImage = Image.fromarray(open_out)
    # 获取图片的字符串
    text = tess.image_to_string(textImage)
    print(f'识别结果为：{text}')


# 读取要识别的验证码
src = cv.imread('./5809.png')
# 设置窗口名字，窗口_自动调整大小
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
# 打开验证码图片
cv.imshow("input image", src)
# 识别验证码
recognize_text()
# 显示出图像后将暂停，等待接收一个键盘输入
cv.waitKey(0)
# 销毁所有窗口
cv.destroyAllWindows()
