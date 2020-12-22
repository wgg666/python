# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    try:
        app.run(host='192.168.100.3', port=8000, debug=True)
    except OSError:
        print('以一种访问权限不允许的方式做了一个访问套接字的尝试=>端口被占用！！！')