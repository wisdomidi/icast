from sqlalchemy import (Column, create_engine, Date, ForeignKey, Integer, String)
from flask_sqlalchemy import SQLAlchemy
import json
import os
from datetime import datetime

# database_path = os.environ['DATABASE_URL']

database_path = 'postgres://wisdomidi:Sososoweto2010@localhost:5432/castingdb'
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #db.create_all()
    
class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    def actor_to_dictionary(self):
        return{
            'id': self.id,
            'first name': self.first_name,
            'last name': self.last_name,
            'age': self.age,
            'gender': self.gender
        }

    def __repr__(self):
        return ("Actor Id: " + {self.id} +
                ", First Name: " + {self.first_name} +
                ", age: " + {self.age} +
                ", gender: " + {self.gender} +
                ", Last Name: " + {self.last_name}
                )

class Movie(db.Model):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    actor_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    release_date = db.Column(db.DateTime(), default=datetime.utcnow)

    def movie_to_dictionary(self):
        return{
            'id': self.id,
            'actor_id': self.actor_id,
            'title': self.title,
            'release_date': self.release_date
        }


def __repr__(self):
        return ("movie Id: " + {self.id} +
                ", actor_id: " + {self.actor_id} +
                ", title: " + {self.title} +
                ", release_date: " + {self.release_date})