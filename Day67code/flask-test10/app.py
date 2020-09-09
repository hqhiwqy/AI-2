# ==========  =====================  ==================================
# HTTP 方法           行为                              示例
# ==========  =====================  ==================================
# GET         获取资源的信息               http://example.com/api/orders
# GET         获取某个特定资源的信息         http://example.com/api/orders/123
# POST        创建新资源                  http://example.com/api/orders
# PUT         更新资源                    http://example.com/api/orders/123
# DELETE      删除资源                    http://example.com/api/orders/123
# ==========  ====================== ==================================


from flask import Flask, jsonify
from models import User, db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
# db = SQLAlchemy(app)


@app.route('/ping')
def ping():
    """测试"""
    return 'pong'


@app.route('/api/users', methods=['GET'])
def get_users():
    """获取所有的用户信息"""
    users = User.query.all()
    return jsonify([x.to_json() for x in users])
