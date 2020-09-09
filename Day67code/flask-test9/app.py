# ==========  ===============================================  =============================
# HTTP 方法   URL                                              动作
# ==========  ===============================================  ==============================
# GET         http://[hostname]/todo/api/tasks                  检索任务列表
# GET         http://[hostname]/todo/api/tasks/[task_id]        检索某个任务
# POST        http://[hostname]/todo/api/tasks                  创建新任务
# PUT         http://[hostname]/todo/api/tasks/[task_id]        更新任务
# DELETE      http://[hostname]/todo/api/tasks/[task_id]        删除任务
# ==========  ================================================ =============================


from flask import Flask, jsonify, abort, request


app = Flask(__name__)

# 任务列表
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': True
    }
]


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """获取所有的任务列表"""
    return jsonify({'code':0,'tasks':tasks})


@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task(id):
    """获取单个任务"""
    task = list(filter(lambda x: x['id'] == id, tasks))
    # 判断id是否存在
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/api/tasks', methods=['POST'])
def add_task():
    """添加单个任务"""
    if not request.json or not 'title' in request.json:
        abort(400)

    tasks.append(request.json)

    return jsonify({'code': 0, 'task': tasks})


@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """删除单个任务"""
    task = list(filter(lambda x: x['id'] == id, tasks))
    if len(task) == 0:
        abort(404)

    tasks.remove(task[0])
    return jsonify({'code': 0, 'task': task[0]})


@app.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """更新单个任务"""
    task = list(filter(lambda x: x['id'] == id, tasks))
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json:
        abort(400)
        if 'description' in request.json:
            abort(400)
            if 'done' in request.json and type(request.json['done']) is not bool:
                abort(400)
    task[0]['done'] = request.json.get('done', task[0]['done'])
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run(debug=True)