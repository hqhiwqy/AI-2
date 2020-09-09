# ==========  =====================  ==================================
# HTTP 方法           行为                              示例
# ==========  =====================  ==================================
# GET         获取资源的信息               http://example.com/api/orders
# GET         获取某个特定资源的信息         http://example.com/api/orders/123
# POST        创建新资源                  http://example.com/api/orders
# PUT         更新资源                    http://example.com/api/orders/123
# DELETE      删除资源                    http://example.com/api/orders/123
# ==========  ====================== ==================================


from flask import Flask, jsonify, abort, request
from werkzeug.security import generate_password_hash
from models import db, User

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)


@app.route('/ping')
def ping():
    """测试"""
    return 'pong'


@app.route('/api/users', methods=['GET'])
def get_users():
    """获取所有的用户信息"""
    users = User.query.all()
    return jsonify([x.to_json() for x in users])


@app.route('/api/users/<int:pk>', methods=['GET'])
def get_user(pk):
    """获取单个用户"""
    user = User.query.get(pk)

    if user is None:
        abort(404)

    return jsonify(user.to_json())


@app.route('/api/users', methods=['POST'])
def add_user():
    """新增单个用户"""
    if not request.json or \
            not 'name' in request.json or \
            not 'password' in request.json or \
            not 'nickname' in request.json or \
            not 'email' in request.json:
        abort(400)

    user = User(name=request.json['name'],
                password=request.json['password'],
                nickname=request.json['nickname'],
                email=request.json['email'])

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_json())


@app.route('/api/users/<int:pk>',methods=['DELETE'])
def delete_user(pk):
    """删除单个用户"""
    user = User.query.get(pk)

    if user is None:
        abort(404)

    db.session.delete(user)
    db.session.commit()

    return jsonify(user.to_json())


@app.route('/api/users/<int:pk>', methods=['PUT'])
def update_user(pk):
    """更新单个用户"""
    user = User.query.get(pk)
    if user is None:
        abort(404)

    if not request.json or \
            not 'name' in request.json or \
            not 'password' in request.json or \
            not 'nickname' in request.json or \
            not 'email' in request.json:
        abort(400)

    # print(type(user))
    user.name = request.json['name']
    user.password = generate_password_hash(request.json['password'])
    user.nickname = request.json['nickname']
    user.email = request.json['email']

    db.session.commit()

    return jsonify(user.to_json())