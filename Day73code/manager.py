from application import app, db, manager
from flask_script import Server
from flask_migrate import Migrate, MigrateCommand
import traceback
import www

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0',
                                        port=app.config['SERVER_PORT'],
                                        use_debugger=app.config['DEBUG']))

if __name__ == "__main__":
    try:
        manager.run()
    except Exception as err:
        traceback.print_exc(err)
