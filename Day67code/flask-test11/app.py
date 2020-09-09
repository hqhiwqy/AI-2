from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文
api = Api(app)


class UserApi(Resource):

    def get(self, id):
        return jsonify({"result": "根据ID获取用户"})

    def put(self, id):
        return jsonify({"result": "根据ID更新用户"})

    def delete(self, id):
        return jsonify({"result": "根据ID删除用户"})


api.add_resource(UserApi, '/api/users/<int:id>', endpoint='user')


class TaskListAPI(Resource):
    def get(self):
        """获取所有的任务列表"""
        return jsonify({"result": "获取所有任务"})

    def post(self):
        """新增单个的任务"""
        return jsonify({"result": "新增单个任务"})


class TaskAPI(Resource):
    def get(self, id):
        """获取单个任务"""
        return jsonify({"result": "获取单个任务"})

    def put(self, id):
        """更新单个任务"""
        return jsonify({"result": "更新单个任务"})

    def delete(self, id):
        """删除单个任务"""
        return jsonify({"result": "删除单个任务"})


api.add_resource(TaskListAPI, '/api/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/api/tasks/<int:id>', endpoint='task')

if __name__ == '__main__':
    app.run(debug=True)
