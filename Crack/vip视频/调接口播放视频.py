from tkinter import Entry
import tkinter.messagebox as msgbox
from urllib import parse
import webbrowser,re
import tkinter as tk
# blob:https://v.qq.com/449405b0-dbe5-418b-b768-caef337b9638
# //*[@id="txplayer_8a929c9a3a438897140ea07c8e9493d3"]/txpdiv[3]/video[1]
class APP():
    def __init__(self, width = 500,height = 300):
        self.w = width
        self.h = height
        self.title = 'vip付费电影免费看'
        self.root = tk.Tk(className=self.title)
        # 地址变量
        self.url = tk.StringVar()
        # 小型框架
        frame_1 = tk.Frame(self.root)
        # 标签
        lable = tk.Label(frame_1,text='视频地址：')
        # 输入框
        Entry = tk.Entry(frame_1,textvariable=self.url,width=35)
        # 播放按钮
        play = tk.Button(frame_1,text='播放',font=('楷体',12),fg='red',width=2,height=1,command=self.video_play)
        frame_1.pack()
        lable.grid(row=0,column=0)
        Entry.grid(row=0,column=1)
        play.grid(row=0,column=2,ipadx=12,ipady=12)

    def video_play(self):
        port = 'http://www.wmxz.wang/video.php?url='
        regx = '^https?:/{2}\w.+$'
        ips = self.url.get()
        if re.match(regx,self.url.get()):
            # 包装
            ip = parse.quote_plus(ips)
            webbrowser.open(port + ip)
        else:
            msgbox.showerror(title='错误警告',message='视频地址无效，请重新输入！')
    def loop(self):
        # 固定窗口大小
        self.root.resizable(True,True)
        self.root.mainloop()

if __name__ == '__main__':
    app = APP()
    app.loop()