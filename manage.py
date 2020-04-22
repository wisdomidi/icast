from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask

from create_app import app
from models import db, Actor, Movie

#print(app)
#app = Flask(__name__)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()