from tkinter import *
import pickle
from tkinter import messagebox

window = Tk()
window.title('测试')
window.geometry('450x300+700+100')

# 标签
Label(window,text='账号').place(x=50,y=150)
Label(window,text='密码').place(x=50,y=190)

var_usr_name = StringVar()
# 账号框默认值
var_usr_name.set('**********@**.com')
var_usr_pwd = StringVar()

# 输入框
entry_usr_name = Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
entry_usr_name = Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_name.place(x=160,y=190)

# 注册
def usr_sign_up():
 
    # 创建一个顶层窗口
    window_sign_up = Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')

    # 账号
    new_name = StringVar()
    new_name.set('**********@qq.com')
    Label(window_sign_up,text='账号').place(x=10,y=10)
    entry_new_name = Entry(window_sign_up,textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    # 密码
    new_pwd = StringVar()
    Label(window_sign_up,text='密码').place(x=10,y=50)
    entry_usr_pwd = Entry(window_sign_up,textvariable=new_pwd,show='*')
    entry_usr_pwd.place(x=150,y=50)

    # 确认密码
    new_pwd_confirm = StringVar()
    Label(window_sign_up,text='确认密码').place(x=10,y=90)
    entry_usr_pwd_confirm = Entry(window_sign_up,textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm .place(x=150,y=90)

    def sign_to_Mofan_Python():
        np = new_pwd.get() #密码
        npf = new_pwd_confirm.get() #确认密码
        nn = new_name.get() #用户名
        with open('F:\\programming\\python\\GUI\\tkinter\\usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
            print(exist_usr_info)
        # 如果两次密码不一致
        if np != npf:   
            messagebox.showerror(message='两次密码不一致')
            # 否则如果用户名存在
        elif nn in exist_usr_info:
            messagebox.showerror(message= nn + '已存在,请更换！！！')
        else:
            # 保存输入的账号密码
            exist_usr_info[str(nn)] = str(np)
            with open('F:\\programming\\python\\GUI\\tkinter\\usrs_info.pickle','wb') as usr_file:
                # 存数据
                pickle.dump(exist_usr_info,usr_file)
                print(exist_usr_info)
                messagebox.showinfo(message='注册成功')
        # 销毁窗口
        window_sign_up.destroy()

    btn_comfirm_sign_up = Button(window_sign_up,text='立即注册',command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150,y=130)
# 登录
def usr_login():
    # 拿账号
    usr_name = var_usr_name.get()
    #拿密码
    usr_pwd = var_usr_pwd.get()
    # 设置管理员
    try:
        with open('F:\\programming\\python\\GUI\\tkinter\\GUI\\tkinter\\usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('F:\\programming\\python\\GUI\\tkinter\\usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
            # 如果用户名正确
    if usr_name in usrs_info:
        # 如果密码正确
        if usr_pwd == usrs_info[usr_name]:
            # 弹窗信息
            messagebox.showinfo(title='Welcome',message='登陆成功' + usr_name)
        else:
            # 弹窗错误
            messagebox.showerror(message='密码错误')
    else:
        # 提示窗口
        is_sign_up = messagebox.askyesno(message=usr_name + '没有注册,是否注册?')
        if is_sign_up:
            usr_sign_up()
# 按钮
btn_login = Button(window,text='注册',command=usr_sign_up)
btn_login.place(x=170,y=230)
btn_sign_up = Button(window,text='登录',command=usr_login)
btn_sign_up.place(x=270,y=230)


window.mainloop()

