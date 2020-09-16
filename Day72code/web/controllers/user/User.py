from flask import Blueprint
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import flash
from common.models.User import User
from werkzeug.security import check_password_hash
from common.libs.UrlManager import UrlManager

route_user = Blueprint('user_page', __name__)


@route_user.route('/')
@route_user.route('/index')
def index():
    """管理员列表页"""
    return render_template('/user/index.html', users=None)


# 登录
@route_user.route('/login', methods=["GET", "POST"])
def login():
    # 如果是POST请求，进行登录处理
    if request.method == "POST":
        # 实现登录功能
        # 1、接收表单提交过来的数据
        username = request.form['username']  # 接收的账号
        password = request.form['password']  # 接收的密码

        # 2、根据接收用户名到user数据表进行查询
        user = User.query.filter_by(login_name=username, status=1).first()

        # 查询一个不存在的用户名返回None
        # 3、判断用户是否存在，如果存在，则进一步需要检测密码是否正确，如果密码检测通过，则登录成功
        if user and check_password_hash(user.login_pwd, password):

            # 登录成功，使用session保存id，同时重定向到首页
            session['isLogged'] = 1
            session['userid'] = user.id
            session['username'] = user.login_name
            return redirect(UrlManager.build_url("/"))
        else:
            # 登录失败，通过flash进行消息提示
            flash("账户或密码不对！")

    return render_template("login.html")


# 退出
@route_user.route('/logout')
def logout():
    session.clear()
    return redirect(UrlManager.build_url("/user/login"))