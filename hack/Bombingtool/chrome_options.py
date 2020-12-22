from selenium import webdriver

class Chrome_options():
    """ 谷歌浏览器驱动配置 """
    chrome_options = webdriver.ChromeOptions()
    chrome_options._arguments = [
        "--no-sandbox",  # 加上这句,就不会报崩溃了
        '--ignore-certificate-errors',  # 忽略证书错误
        # '--headless',# 无头
        '--disable-gpu',  # 禁用-gpu#规避bug
        '--start-maximized'  # 最大化
    ]
    chrome_options._experimental_options = {
        'excludeSwitches': [
            'enable-automation', #排除开关启用自动操作
            'enable-logging', #开启日志
            'load-extension' #加载扩展
        ], 
        'prefs': {#屏蔽'保存密码'提示框
            'credentials_enable_service': False, 
            'profile.password_manager_enabled': False
        },
        'useAutomationExtension': False #去掉开发者警告
    }
chrome_options = Chrome_options()

if __name__ == "__main__":
    chromedriver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    # 打开浏览器
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
    #设置window.navigator.webdriver=undefined
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """
    })

