import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Flask实例
app = Flask(__name__)

# 使用会话前，必须设置秘钥
app.secret_key = os.urandom(24)

app.config.from_object('config.default')

db = SQLAlchemy(app)
