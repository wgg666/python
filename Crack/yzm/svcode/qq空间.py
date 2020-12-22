# coding=utf-8
import threading
import time
import numpy as np
from selenium import webdriver
import requests
import cv2
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://i.qq.com/')

iframe_xpath = {"登录": '//*[@id="login_frame"]', "验证码": '//*[@id="tcaptcha_iframe"]'}
login_info = {"账号": "286110433", "密码": "Xwl/520886/+-*/."}
login_xpath = {"账号": '//*[@id="u"]', "密码": '//*[@id="p"]'}
click_xpath = {"账号密码登录": '//*[@id="switcher_plogin"]', "登录": '//*[@id="login_button"]'}
yzm_xpath = {"验证码背景图": '//*[@id="slideBg"]', "滑块图": '//*[@id="slideBlock"]'}
yzm_path = {'背景图': r'.\Crack\yzm\svcode\imgs\target.png', '滑块图': r'.\Crack\yzm\svcode\imgs\template.png'}


# 进入框架
def goto_iframe(iframe_xpath):
    driver.switch_to.frame(driver.find_element_by_xpath(iframe_xpath))


# 点击
def xpath_click(click_xpath):
    driver.find_element_by_xpath(click_xpath).click()


# 输入
def xpath_send_keys(login_xpath, login_info):
    driver.find_element_by_xpath(login_xpath).send_keys(login_info)


# 获取属性
def get_attribute(yzm_xpath, attribute):
    return driver.find_element_by_xpath(yzm_xpath).get_attribute(attribute)


# xpath获取元素
def by_xpath(xpath):
    return driver.find_element_by_xpath(xpath)


# 登录
def login():
    # 进入到登录的iframe
    goto_iframe(iframe_xpath['登录'])
    # 点击账号密码登录
    xpath_click(click_xpath['账号密码登录'])
    # 输入qq号
    xpath_send_keys(login_xpath['账号'], login_info["账号"])
    # 输入密码
    xpath_send_keys(login_xpath['密码'], login_info["密码"])
    # 点击登录
    xpath_click(click_xpath["登录"])


# 获取验证码背景二进制数据
def get_code_background():
    # # 验证码背景图片地址 
    src = by_xpath(yzm_xpath["验证码背景图"]).get_attribute('src')
    response = requests.get(src)
    # 二进制背景图
    target = response.content
    with open(yzm_path['背景图'], 'wb') as f:
        f.write(target)


# 滑块二进制数据
def get_code_slider():
    print('正在下载验证码滑块！！！')
    # time.sleep(1)
    # # 按钮图片地址
    src = get_attribute(yzm_xpath["滑块图"], 'src')
    response = requests.get(src)
    # 二进制按钮图
    template = response.content
    with open(yzm_path['滑块图'], 'wb') as f:
        f.write(template)


# 匹配缺口
def mvcode():
    print('开始匹配滑块和验证码的缺口的最佳位置！！！')
    # 读取背景图
    target_rgb = cv2.imread(yzm_path["背景图"])
    # 读取滑块图
    template_rgb = cv2.imread(yzm_path["滑块图"], 0)
    #去掉多余的黑色保留灰色
    # template_rgb = template_rgb[template_rgb.any(1)]
    # 背景灰度处理
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_RGB2GRAY)
    # 匹配两张图片(背景，滑块，算法)
    # 获得最差和最佳匹配位置 #这个算法精度最高，匹配最慢
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)
    # 获取背景图在网页上的大小
    img_target = by_xpath(yzm_xpath['验证码背景图'])
    size = img_target.size
    w1 = size['width']
    # 原图大小
    w2 = target_rgb.shape[1]
    # 偏移量(计算原图在网页上的缩放)
    x = int((value[2][0] + 23) * w1 / w2) - 29
    print(f'最佳位置为：{x}\n开始移动滑块！！！')
    return x


# 拖动滑块
def Drag_the_slider(x):
    # 获取滑块
    ele_template = by_xpath(yzm_xpath["滑块图"])
    action = ActionChains(driver)
    # 按住滑块不放
    action.click_and_hold(ele_template).perform()
    # 拖动
    action.move_by_offset(x, 0).perform()
    # 释放鼠标
    action.release().perform()


if __name__ == '__main__':
    try:
        login()  # 登录
        # 进入滑块验证码的iframe
        goto_iframe(iframe_xpath['验证码'])
        # 单进程多线程
        t1 = threading.Thread(target=get_code_background, )
        t2 = threading.Thread(target=get_code_slider)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        # 验证码缺口x轴位置
        x = mvcode()
        Drag_the_slider(x)  # 拖动滑块到缺口位置
        print('登录成功！！！')
    except:
        print('登录成功！！！')
