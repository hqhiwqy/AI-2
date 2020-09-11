from app import app, db
from controllers.admin import admin_route
from controllers.home import home_route
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# 注册admin蓝图
app.register_blueprint(admin_route, url_prefix="/admin")

# 注册index蓝图
app.register_blueprint(home_route, url_prefix="/")


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
