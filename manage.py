from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask

from app import app
from models import Actor, Movie, db

app = Flask(__name__)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()