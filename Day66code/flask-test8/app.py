import os
from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_moment import Moment

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:hao7883370@192.168.81.129:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['PERMANENT_SESSION_LIFETIME'] = 7*24*60*60
# PERMANENT_SESSION_LIFETIME = timedelta(days=4)
app.permanent_session_lifetime = timedelta(seconds=7*24*60*60)
db = SQLAlchemy(app)
moment = Moment(app)




# 创建 User 模型


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(20), unique=True)
    passwd = db.Column(db.String(100), unique=True)

    def __init__(self, account, passwd):
        self.account = account
        self.passwd = generate_password_hash(passwd)  # 密码加密


@app.route("/ping")
def ping():
    return 'pong'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']
        user = User.query.filter_by(account=account).first()
        if user and check_password_hash(user.passwd, password):
            session.permanent = True
            session['isLogged'] = 1
            session['account'] = account
            return redirect(url_for('index'))
        else:
            flash("账号或密码错误！")

    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop('isLogged', None)
    session.pop('account', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)