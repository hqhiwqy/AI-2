from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "\x97\x1fY\xf4\x9b\xad\xcd\x9f\x81\xc8&\x1c\xf4\x15f\x0cE]\xd8\xac\x18\x84\x14"


# 首页
@app.route("/")
def index():
    if "account" in session:
        return render_template("index.html", account=session['account'])
    return render_template("index.html")


# 登录页
@app.route("/login", methods=['GET', 'POST'])
def login():
    # 判断是否为POST请求
    if request.method == "POST":
        # 模拟登录,这里假设登陆成功
        session['account'] = request.form['account']
        # 重定向到首页
        return redirect(url_for('index'))
    return render_template("login.html")


# 退出
@app.route("/logout")
def logout():
    session.pop('account', None)
    return redirect(url_for('index'))


# 404页
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)
