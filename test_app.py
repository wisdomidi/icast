import os
import unittest
import json
import http.client
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie,db
#from app import APP

# MEMBER USER GENERATED FOR TESTING PURPOSES ONLY
# HAS ALL PERMISSIONS:
# "get:actors", "get:movies",
# "post:actors", "post:movie", "patch:movie", "delete:movie"
MEMBER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1USTJRVEE1TVRZM00wVTVRa0k1TVRJd1JUQkZRVEJEUVRjd05URkVNRVE1UVVVeE1rVTBSQSJ9.eyJpc3MiOiJodHRwczovL3dpc2RvbWlkaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OTRjNzQ3Mjg0ZGIwYzhkNDkzYTg1IiwiYXVkIjoiaWNhc3QiLCJpYXQiOjE1ODc0NDU1MzEsImV4cCI6MTU4NzUzMTkzMSwiYXpwIjoiU1Q2Nkl1bHZYM3ZDbnJMdEpneWd4OW1JS2tuRWtpd1EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.C3UniiV1DigOfIZnRzG9OdznKsPJc_iNN1LYlNjkMFSU2BNkbegj3zIBySc6_wBvNVl_5bSps1JaQdC91Z7IU5FyYvtO2owYabJn6zDabGBlYnMgpd3nnDQncidXVGBG6c8imHJ6Vo7yhedEy32f6T3vLJlJGVfc_Lc7SObvsMzr-F-ypg-Uiu13sxtTFysUWTn-xBCPx1CZ0DHvjrPkscYPY2P5IrMkO_RvC4lH0yygZjAcpYzIEE7cfBnqCdPQgtOAeoMC63WqfFzT2319SWbYPAvs-sc36Z42IgD4R8W_m6WMWW6YNqO8eWh34FXo8Xjq75wsgNBj0g3nHLY33Q'

# PUBLIC USER GENERATED FOR TESTING PURPOSED ONLY
# "get:actors", "get:movies",
PUBLIC_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1USTJRVEE1TVRZM00wVTVRa0k1TVRJd1JUQkZRVEJEUVRjd05URkVNRVE1UVVVeE1rVTBSQSJ9.eyJpc3MiOiJodHRwczovL3dpc2RvbWlkaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OTQ0OWY5N2Q4NzAwYzkxODZiMmVjIiwiYXVkIjoiaWNhc3QiLCJpYXQiOjE1ODc0NDU4MjYsImV4cCI6MTU4NzUzMjIyNiwiYXpwIjoiU1Q2Nkl1bHZYM3ZDbnJMdEpneWd4OW1JS2tuRWtpd1EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.HFjsVeQ0ylaXvGVaCq2OVRa5GWJexrVBWTDo35jduwCys8ZU7-LSeq21hDcH5m6C1ifdgzTWbmNGMjoUhVQaAzqUC3cgEBHT5wC3JAXOuiu1Uo4tm4UUMc4-lCJ__x9jCw9N-qmdX081IHo8j49V1QtW2QpLIVgI_sdZLLY15bTVwFMLqA3aeBimc-St8RxJWrz1M_Q6jkfqax4nO9vRRR6vbpa2-8evNu2h7JNx1zBTMEYouHt17KuHA0TFJ7TvMukQxYj9netcdNvpREhQxYI-IPN197ZrYZQFpkUcvgk9noinpeYOzc0nY0HozJHGt3O5HeI3ad-jyFaelGiZXQ'


class IcastTestCase(unittest.TestCase):

    def setUp(self):
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wisdomidi:Sososoweto2010@localhost:5432/castingdb_test'
        #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        #db.app = app
        #db.init_app(app)
        
        self.app = create_app()
        #self.client = self.app.test_client()
        
        self.client = self.app.test_client
        self.headers_member = {
            'Content-Type': 'application/json',
            'Authorization': MEMBER_TOKEN}
        self.headers_public = {
            'Content-Type': 'application/json',
            'Authorization': PUBLIC_TOKEN}

        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Execute after each test
        pass

    # GET ENDPOINTS
    def test_get_actors_member(self):
        response = self.client().get(
            '/actors',
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_get_actors_public(self):
        response = self.client().get(
            '/actors',
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    def test_get_movies_member(self):
        response = self.client().get(
            '/movies',
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_get_movies_public(self):
        response = self.client().get(
            '/movies',
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    # PUT ENDPOINTS
    def test_add_actor_member(self):
        new_actor = {
            "first_name": "Amelia",
            "last_name": "Boone",
            "age": "77",
            "gender": "male"

        }

        response = self.client().post(
            '/actors',
            json=new_actor,
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_add_actor_public(self):
        new_actor = {
            "first_name": "Amelia",
            "last_name": "Boone",
            "age": "77",
            "gender": "male"
        }

        response = self.client().post(
            '/actors',
            json=new_actor,
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    def test_add_movie_member(self):
        new_movie = {
            "actor_id": "1",
            "tittle": "newtitle",
            "release_date": "2020-08-09"
        }

        response = self.client().post(
            '/movies',
            json=new_movie,
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_add_movie_public(self):
        new_movie = {
            "actor_id": "1",
            "tittle": "newtitle",
            "release_date": "2020-08-09"
        }

        response = self.client().post(
            '/movies',
            json=new_movie,
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)

    # PATCH ENDPOINT
    def test_update_movie_member(self):
        updated_movie = {
            "actor_id": "1"
        }

        response = self.client().patch(
            '/movies/1',
            json=updated_movie,
            headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_update_movie_public(self):
        updated_movie = {
            "actor_id": "1"
        }

        response = self.client().patch('/movies/1', json=updated_movie)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    # DELETE ENDPOINT
    def test_delete_movie_member(self):
        response = self.client().delete('/movies/1', headers=self.headers_member)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_delete_movie_public(self):
        response = self.client().delete(
            '/movies/1',
            headers=self.headers_public)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 401)


# Make the tests conviently executable
if __name__ == "__main__":
    unittest.main()