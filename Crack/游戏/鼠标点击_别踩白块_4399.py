#coding=utf-8
import pyautogui
import time

# 安全模式 鼠标移动到顶点就结束
pyautogui.FAILSAFE = True
time.sleep(3)
# 坐标 和图片长和宽
while True:
    region=(488,419,479,38)
    im = pyautogui.screenshot(region=region) #截图
    im.save('test.png') #保存图片
    #第一块： x: 488/4/2=61 #y=38 /2=19
    #第二块：x=122+61=183 y=19
    # 第三块：x=122*2+61=305 y=19
    # 第三块：x=122*3+61=427
    for i in range(61,428,122): #61+122+122+。。。427 end
        px = im.getpixel((i, 19))
        print(px)
        if px[0] == 1: #如果是黑色
            pyautogui.click(region[0]+i,+region[1]+19)
