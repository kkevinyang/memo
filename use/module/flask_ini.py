#!/usr/bin/env python#
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)  # Flask类构造函数只需一个指定的参数即主模块的名字，可用这个参数决定程序的根目录，以便确定相对路径


@app.route('/')  # 把修饰函数定义为路由，访问根目录时激发index函数，即‘响应’
def index():  # 视图函数
    return"<h1>Hello World!</h1>"


@app.route('/user/<name>')  # 动态名字
def user(name):
    return'<h1>Hello,%s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)  # 启动调试模式
