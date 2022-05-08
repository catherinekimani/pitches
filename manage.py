from app import create_app,db
from flask_script import Manager,Server
from app.models import User
from flask_migrate import Migrate,MigrateCommand

# create app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()