# 定义和创建Flask应用实例

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


class Application(Flask):
    def __init__(
        self,
        import_name,
        static_folder=None,
        template_folder=None,
        root_path=None
    ):
        super().__init__(
            import_name=import_name,
            static_folder=static_folder,
            template_folder=template_folder,
            root_path=root_path)
        self.config.from_object('config.base_setting')
        self.config.from_object('config.local_setting')
        db.init_app(self)


# 实例化数据库
db = SQLAlchemy()
# db = SQLAlchemy(app)


# os.getcwd() 获取当前脚本所在的目录
app = Application(
    __name__,
    static_folder=os.getcwd() + '/web/static/',
    template_folder=os.getcwd() + '/web/templates/',
    root_path=os.getcwd()
)


@app.route('/ping')
def ping():
    return 'pone'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()