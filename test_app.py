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
EXECUTIVE_DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1USTJRVEE1TVRZM00wVTVRa0k1TVRJd1JUQkZRVEJEUVRjd05URkVNRVE1UVVVeE1rVTBSQSJ9.eyJpc3MiOiJodHRwczovL3dpc2RvbWlkaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OTRjNzQ3Mjg0ZGIwYzhkNDkzYTg1IiwiYXVkIjoiaWNhc3QiLCJpYXQiOjE1ODc1OTk0MjcsImV4cCI6MTU4NzY4NTgyNywiYXpwIjoiU1Q2Nkl1bHZYM3ZDbnJMdEpneWd4OW1JS2tuRWtpd1EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.E1y4MSWiV86XT4KRhkbgpI8R4rluVEyEAWUW1_K75gNE2Oc5ClWH0WRaLp39Sisu1JNfay88Tal9LoOJEbI2j_unb2cUv8ceo36MI57WA93Z70nlA-fLq8jiMIqxNYY9db7X3S5QjSmphQoDYqagxRUx10dvih1c_CThrAhqeS01RCEVyT10XR_LjLYhKWbc8YRhPYeMyYPzakGZAJzWhgsPPLeYdj0vrW8qsXRThjh1SBxmZw7CsMEH3BsUcVGFXE5LmGD-3PRG4PYtNYwZa1JYZCD_QsIq1azfucYKNp1BVDZ_xu87rW4TAyPvpnE-kGKiEpma50XcveAe9k69Iw'
MEMBER_TOKEN = ''
# PUBLIC USER GENERATED FOR TESTING PURPOSED ONLY
# "get:actors", "get:movies",
PUBLIC_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1USTJRVEE1TVRZM00wVTVRa0k1TVRJd1JUQkZRVEJEUVRjd05URkVNRVE1UVVVeE1rVTBSQSJ9.eyJpc3MiOiJodHRwczovL3dpc2RvbWlkaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OTQ0OWY5N2Q4NzAwYzkxODZiMmVjIiwiYXVkIjoiaWNhc3QiLCJpYXQiOjE1ODc0NDU4MjYsImV4cCI6MTU4NzUzMjIyNiwiYXpwIjoiU1Q2Nkl1bHZYM3ZDbnJMdEpneWd4OW1JS2tuRWtpd1EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.HFjsVeQ0ylaXvGVaCq2OVRa5GWJexrVBWTDo35jduwCys8ZU7-LSeq21hDcH5m6C1ifdgzTWbmNGMjoUhVQaAzqUC3cgEBHT5wC3JAXOuiu1Uo4tm4UUMc4-lCJ__x9jCw9N-qmdX081IHo8j49V1QtW2QpLIVgI_sdZLLY15bTVwFMLqA3aeBimc-St8RxJWrz1M_Q6jkfqax4nO9vRRR6vbpa2-8evNu2h7JNx1zBTMEYouHt17KuHA0TFJ7TvMukQxYj9netcdNvpREhQxYI-IPN197ZrYZQFpkUcvgk9noinpeYOzc0nY0HozJHGt3O5HeI3ad-jyFaelGiZXQ'

CASTING_ASISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1USTJRVEE1TVRZM00wVTVRa0k1TVRJd1JUQkZRVEJEUVRjd05URkVNRVE1UVVVeE1rVTBSQSJ9.eyJpc3MiOiJodHRwczovL3dpc2RvbWlkaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OTQzYmI5N2Q4NzAwYzkxODZiMDkxIiwiYXVkIjoiaWNhc3QiLCJpYXQiOjE1ODc1OTk2MzMsImV4cCI6MTU4NzY4NjAzMywiYXpwIjoiU1Q2Nkl1bHZYM3ZDbnJMdEpneWd4OW1JS2tuRWtpd1EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.QSoFuH0JfM1lDBECMIWzWMkdRgaayCFpZOh0QtMsiEo_xs_Xxu_YX1ignfbLqKaX8iwde0uxzXZSSKi6DC8z_oG-Kd1amyuxK0XDEKy1R2aLDhwCWZkTjhWBC8dWRZ62umS1hQoj2AdlIFbhhWzYvaPBiYhY8PlZKjK_FipN8Uqk1m2OLVumEUH54DBY_YeUiSD5tOqswOcoEzHH4CmFwBQjO02-tIdhVxr-aQN78rhEFJ69KB-mK8PKiZUpDcPVlTltX8bFbnV4uVqImLbuQepx4SAppBkg1DNLknCQuE-fXx0zejguWFCZRJDA5RO5sRY3CvO9-xqCe1m2CRWLYw'


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