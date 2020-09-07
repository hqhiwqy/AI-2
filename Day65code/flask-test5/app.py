from flask import Flask, render_template, session, redirect, url_for

import functools

import os

app = Flask(__name__)

app.secret_key = os.urandom(24)


def login_require(f):
    """登录访问控制装饰器"""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # 判断是否登录
        if 'isLogged' not in session or session['isLogged'] != 1:
                 return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper


@app.route("/")
def index():
    return render_template('home/index.html')


@app.route("/login")
def login():
    # 模拟登录
    session['isLogged'] = 1
    return render_template('home/login.html')


@app.route("/center")
@login_require
def center():
    return render_template('home/center.html')


if __name__ == '__main__':
    app.run(debug=True)