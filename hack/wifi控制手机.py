import uiautomator2

'''
安装：
pip install --pre uiautomator2
pip install pillow
初始化：安装apk
python -m uiautomator2 init
可视化安装：
pip install --pre --upgrade weditor
启动可视化：
python -m weditor
'''

import uiautomator2 as u2

d = u2.connect('192.168.1.110')
# resourceId="com.miui.home:id/icon_icon",
d(description="微信").click()