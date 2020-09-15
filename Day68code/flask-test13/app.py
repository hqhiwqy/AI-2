import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 实例化Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# 使用会话前，必须设置秘钥
app.secret_key = os.urandom(24)

# 导入配置文件
app.config.from_object('config.default_setting')

# 实例化数据库
db = SQLAlchemy(app)