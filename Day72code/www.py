# 统一注册蓝图文件

from application import app
from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.interceptors.AuthInterceptor import *

# 1.注册后台首页蓝图
app.register_blueprint(route_index, url_prefix="/")

# 2.注册用户管理首页蓝图
app.register_blueprint(route_user, url_prefix='/user')