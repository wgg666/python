# coding=utf-8
from email.header import Header  # 完善邮件内容
from email.mime.text import MIMEText  # 创建邮件格式
from smtplib import SMTP_SSL


def send_email(to_addr, Subject, text):
    email_info = {
        "邮箱服务器": 'smtp.qq.com',
        "发件账号": '2861104332@qq.com',
        "授权码": 'uybcgdjcaptddehc',
        "发件人": '匿名用户'
    }
    # text发送的内容
    email = MIMEText(text, 'plain', 'utf-8')  # 创建一份邮件
    email['Subject'] = Header(Subject)  # 主题
    email['From'] = Header(email_info["发件人"])  # 显示的发件人邮箱
    email['To'] = Header(to_addr)  # 显示的收件人邮箱

    # 连接服务器
    qq_email = SMTP_SSL(email_info['邮箱服务器'])  # 连接服务器
    qq_email.login(email_info['发件账号'], email_info['授权码'])  # 登录账号
    qq_email.sendmail(email_info['发件账号'], to_addr, email.as_string())  # 发送邮件
    qq_email.quit()  # 退出
    print(email)


if __name__ == '__main__':
    for i in range(5):
        send_email('2861104332@qq.com', '马保国的闪电五连鞭', '年轻人，不讲武德')
        print('邮件发送成功')
