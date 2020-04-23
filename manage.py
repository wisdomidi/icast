from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import db, Actor, Movie
#from models import setup_db, Actor, Movie, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()