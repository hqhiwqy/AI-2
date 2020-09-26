# 后台权限统一拦截器

from application import app
from flask import request
from flask import session
from flask import g
from flask import redirect
from common.models.User import User
from common.libs.UrlManager import UrlManager
import re

# @app.before_request 在请求(request)进入视图函数之前执行
@app.before_request
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']

    path = request.path

    # app.logger.debug(path)

    # 登录前需要忽视的 URL
    pattern = re.compile("|".join(ignore_check_login_urls))

    if pattern.match(path):
        return

    # 登录后需要忽视的URL
    pattern = re.compile("|".join(ignore_urls))

    # 判断是否登录
    user_info = check_login()

    g.current_user = None

    if user_info:
        # 如果已经登录，则将用户信息存储到全局变量 g 中的 current_user
        g.current_user = user_info
        if pattern.match(path):
            return redirect(UrlManager.build_url('/'))

    if pattern.match(path):
        return

    # 如果没有登录，则重定向到登录页
    if not user_info:
        return redirect(UrlManager.build_url('/user/login'))
    return


def check_login():
    """判断是否登录"""
    isLogged = session['isLogged'] if 'isLogged' in session else None

    if isLogged is None:
        return False

    # 根据session中存储的userid来查询登录用户的信息
    try:
        user_info = User.query.get(session['userid'])
    except Exception as Err:
        return False

    if user_info is None:
        return False

    if user_info.status != 1:
        return False

    return user_info
