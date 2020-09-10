import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 实例化Flask
app = Flask(__name__)

# 使用会话前，必须设置秘钥
app.secret_key = os.urandom(24)

# 导入配置文件
app.config.from_object('config.default_setting')

# 实例化数据库
db = SQLAlchemy(app)