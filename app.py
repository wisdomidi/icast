import os
import sys
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import logging
from auth import AuthError, requires_auth
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from models import setup_db, Actor, Movie, db
from models import db, Actor, Movie


database_path = 'postgres://ujpfkhwocykutn:2e3a7ecf456796cf946b1d2e71eb58cec6c127909b1fe4e803ce72da09bfcce0@ec2-54-147-209-121.compute-1.amazonaws.com:5432/de7h7cmbl03cua'

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #db.create_all()


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    migrate = Migrate(app, db) # this


#   get actors 
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(token):
        actors = Actor.query.order_by(Actor.last_name).all()

        return jsonify({
            'success': True,
            'actors': [
                actor.actor_to_dictionary()
                for actor in actors
                ],
            'total_actors': len(actors)
        })


#    get movies 
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(token):
        movies = Movie.query.order_by(Movie.actor_id).all()

        return jsonify({
            'success': True,
            'movies': [movie.movie_to_dictionary() for movie in movies],
            'total_movies': len(movies)
        })



#     post actors
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(token):
        body = request.get_json()

        first_name = body.get('first_name', None)
        last_name = body.get('last_name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        if not ('first_name' in body):
            abort(404)

      #error = True
        try:
            actor = Actor(
                first_name=first_name, last_name=last_name, age=age, gender=gender
                        )
            db.session.add(actor)
            db.session.commit()

            return jsonify({
                'success': True,
                'created actor_id': actor.id,
                'total_actor': len(Actor.query.all())
            })
        except:
            abort(422)

        finally:
            db.session.close()

#   post movies
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movies(token):
        body = request.get_json()

        actor_id = body.get('actor_id', None)
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        if not ('actor_id' in body):
            abort(404)

        try:
            movie = Movie(actor_id=actor_id, title=title, release_date=release_date
                        )

            db.session.add(movie)
            db.session.commit()

            return jsonify({
                'success': True,
                'created movie_id': movie.id,
                'total_movies': len(Movie.query.all())
            })
        except:
            abort(422)

        finally:
            db.session.close()    

#   patch movies
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(token, movie_id):
        movie = Movie.query.get(movie_id)

        if not movie:
            abort(404)

        try:
            body = request.get_json()

            actor_id = body.get('actor_id', None)
            title = body.get('title', None)
            release_date = body.get('release_date', None)

            if actor_id:
                movie.actor_id = actor_id
            if title:
                movie.title = title
            if release_date:
                movie.release_date = release_date

            db.session.add(movie)
            db.session.commit()

            return jsonify({
                'success': True,
                'updated movie_id': movie_id,
            })
        except:
            abort(422)

        finally:
            db.session.close()

# delete movies
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    #@requires_auth('delete:movie')
    def delete_movie(movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            db.session.delete(movie)
            db.session.commit()

            return jsonify({
                'success': True,
                'deleted_movie_id': movie_id,
                'total_movies_remaining': len(Movie.query.all())
            })
        except:
            abort(422)

        finally:
            db.session.close()

#   hello world test
    @app.route('/')
    def hello_world():
        return "Hello, Viewer, You are a public user so this is the only page you can see for now!"


# error handlers 
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized'
        }, 401)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }, 404)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }, 422)

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error
        }, error.status_code)


    return app

APP = create_app()

if __name__ == '__main__':
    #APP.run(host='0.0.0.0', port=8080, debug=True)
    app.run()
