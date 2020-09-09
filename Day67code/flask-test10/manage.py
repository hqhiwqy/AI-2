from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import db

migrate = Migrate(app, db)
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()