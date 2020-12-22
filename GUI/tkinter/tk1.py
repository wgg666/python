from tkinter import *
from 爬虫.py.云代理 import *
class APP:
    def __init__(self, width=250, height=120, x=700, y=100):
        self.root = Tk()
        self.root.title('爬代理IP')
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        # 小型框架
        frame = Frame(self.root)

        self.var = StringVar()
        # var.set('爬取了9页,IP数量：101')

        # 标签
        label = Label(frame, text="URL")
        label2 = Label(frame,textvariable=self.var)
        entry = Entry(frame)

        hi_there = Button(frame, text="开始爬取", fg="blue", command=self.say_hi)

        frame.pack()
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        hi_there.grid(row=0, column=2)
        label2.grid(row=1,column=1)
    def say_hi(self):
        ip3366 = Ip3366()
        # 爬IP线程池
        ip3366.Create_thread_pool(8, ip3366.get_ip, ip3366.base_urls)
        end1_time = time.time()
        print(ip3366.proxies_list)
        # print(f'爬取IP耗时{end1_time - ip3366.start1_time}秒')

        # 清洗ip线程池
        ip3366.Create_thread_pool(10, ip3366.check_ip, ip3366.proxies_list)
        end2_time = time.time()
        # print(f'可用IP池：{ip3366.can_use}\n可用IP数量：{len(ip3366.can_use)}')
        # print(f'清洗IP耗时{end2_time - ip3366.start2_time}秒')
        self.var.set(
            f'爬取了{len(ip3366.base_urls)}页,\
            IP数量：{len(ip3366.proxies_list)}\n'
            f'爬取IP耗时{end1_time - ip3366.start1_time}秒\n'
            f'可用IP池：{ip3366.can_use}\n'
            f'可用IP数量：{len(ip3366.can_use)}\n'
            f'清洗IP耗时{end2_time - ip3366.start2_time}秒')

    def loop(self):
        # 固定窗口大小
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == "__main__":
    app = APP()
    app.loop()
