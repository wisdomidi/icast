# Casting Agency Capstone Project for Udacity

The Casting Agency API models a company that is responsible for creating movies and managing/assigning actors to those movies. This api is responsible for checking permissions and handling CRUD for an Actor and Movie model/

### Getting Started

Installing Dependencies
Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs

### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the root directory of this project and running:

> pip install -r requirements.txt

This will install all of the required packages we selected within the requirements.txt file.

After installing the dependencies, execute the bash file setup.sh to set the user jwts, auth0 credentials and the remote database url by naviging to the root directory of this project and running:
```
> source setup.sh


### Key Dependencies

Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.
```
SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

jose JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Running the server

From within the root directory first ensure you are working using your created virtual environment.

> To run the server, execute:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.

API Reference

Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource not found."
}
```
The API will return three error types with multiple different error messages when requests fail:
```
400: Bad Request

400: Permissions were not included in the JWT.

400: Unable to parse authentication token.

400: Unable to parse authentication token.

400: Unable to find the appropriate key.

401: Authorization header is expected.

401: Authorization header must start with "Bearer".

401: Token not found.

401: Authorization header must be bearer token.

401: Authorization malformed.

401: Token expired.

401: Incorrect claims. Please, check the audience and issuer.

403: Permission denied.

404: Resource Not Found.
```

### Endpoints
GET '/actors'
Fetches a list of actors.

```
{
  'success': True,
  'actors': [
    {
      id: 1,
      name: 'Actor 1',
      age: 30,
      gender: 'male'
    }
  ]
}
```
GET '/movies'
Fetches a list of movies.


```
{
  'success': True,
  'movies': [
    {
      id: 1,
      title: 'New Movie 1',
      release_date: '2021-10-1 04:22'
    }
  ]
}
```
POST '/actors'
Create a new actor.
Request Arguments: { name: String, age: Integer, gender: String }.
Returns: An object with success: True and the new actor inside an array.
```
{
  'success': True,
  'actors': [
    {
      id: 2,
      name: 'Actor 2',
      age: 28,
      gender: 'Female'
    }
  ]
}
```
POST '/movies'
Create a new movie.
Request Arguments: { title: String, release_date: DateTime }.
Returns: An object with success: True and the new movie inside an array.
```
{
  'success': True,
  'movies': [
    {
      id: 2,
      title: 'New Movie 2',
      release_date: '2022-10-1 04:22'
    }
  ]
}
```
Patch '/actors/<actor_id>'
Update an actor.
Request Arguments: { name: String, age: Integer, gender: String }.
Returns: An object with success: True and the updated actor inside an array.
```
{
  'success': True,
  'actors': [
    {
      id: 1,
      name: 'Updated Actor',
      age: 50,
      gender: 'Male'
    }
  ]
}
```
Patch '/movies/<movie_id>'
Update a movie.
Request Arguments: { title: String, release_date: DateTime }.
Returns: An object with success: True and the updated movie inside an array.
```
{
  'success': True,
  'movies': [
    {
      id: 1,
      title: 'Updated Movie 1',
      release_date: '2030-10-1 04:22'
    }
  ]
}
```
DELETE '/actors/<actor_id>'
Removes an actor from the database.
Request Parameters: question id slug.
Returns: An object with success: True and the id of the deleted actor
```
{
  'success': True,
  'id': 1
}
```
DELETE '/movies/<movie_id>'
Removes a movie from the database.
Request Parameters: question id slug.
Returns: An object with success: True and the id of the deleted movie
```
{
  'success': True,
  'id': 1
}
```
Testing


```
This collection has 3 roles that have specific permissions detailed below.

### Roles

Public
No access

Casting Assistant
get:actors, get:movies

Casting Director
get:actors, get:movies, post:actors, patch:actors, patch:movies, delete:actors

Executive Producer (all permissions)
get:actors, get:movies, post:actors, post:movies, patch:actors, patch:movies, delete:actors, delete:movies
```


#### Running tests locally
To run the tests 
```
createdb casting_test

python test_app.py
```

Tokens for each permission type to check auth0 roles

EXECUTIVE_DIRECTOR_TOKEN = 

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1USTJRVEE1TVRZM00wVTVRa0k1TVRJd1JUQkZRVEJEUVRjd05URkVNRVE1UVVVeE1rVTBSQSJ9.eyJpc3MiOiJodHRwczovL3dpc2RvbWlkaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OTRjNzQ3Mjg0ZGIwYzhkNDkzYTg1IiwiYXVkIjoiaWNhc3QiLCJpYXQiOjE1ODc1OTk0MjcsImV4cCI6MTU4NzY4NTgyNywiYXpwIjoiU1Q2Nkl1bHZYM3ZDbnJMdEpneWd4OW1JS2tuRWtpd1EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.E1y4MSWiV86XT4KRhkbgpI8R4rluVEyEAWUW1_K75gNE2Oc5ClWH0WRaLp39Sisu1JNfay88Tal9LoOJEbI2j_unb2cUv8ceo36MI57WA93Z70nlA-fLq8jiMIqxNYY9db7X3S5QjSmphQoDYqagxRUx10dvih1c_CThrAhqeS01RCEVyT10XR_LjLYhKWbc8YRhPYeMyYPzakGZAJzWhgsPPLeYdj0vrW8qsXRThjh1SBxmZw7CsMEH3BsUcVGFXE5LmGD-3PRG4PYtNYwZa1JYZCD_QsIq1azfucYKNp1BVDZ_xu87rW4TAyPvpnE-kGKiEpma50XcveAe9k69Iw'

CASTING_DIRECTOR_TOKEN = 

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1USTJRVEE1TVRZM00wVTVRa0k1TVRJd1JUQkZRVEJEUVRjd05URkVNRVE1UVVVeE1rVTBSQSJ9.eyJpc3MiOiJodHRwczovL3dpc2RvbWlkaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OTQzYmI5N2Q4NzAwYzkxODZiMDkxIiwiYXVkIjoiaWNhc3QiLCJpYXQiOjE1ODc1OTk2MzMsImV4cCI6MTU4NzY4NjAzMywiYXpwIjoiU1Q2Nkl1bHZYM3ZDbnJMdEpneWd4OW1JS2tuRWtpd1EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.QSoFuH0JfM1lDBECMIWzWMkdRgaayCFpZOh0QtMsiEo_xs_Xxu_YX1ignfbLqKaX8iwde0uxzXZSSKi6DC8z_oG-Kd1amyuxK0XDEKy1R2aLDhwCWZkTjhWBC8dWRZ62umS1hQoj2AdlIFbhhWzYvaPBiYhY8PlZKjK_FipN8Uqk1m2OLVumEUH54DBY_YeUiSD5tOqswOcoEzHH4CmFwBQjO02-tIdhVxr-aQN78rhEFJ69KB-mK8PKiZUpDcPVlTltX8bFbnV4uVqImLbuQepx4SAppBkg1DNLknCQuE-fXx0zejguWFCZRJDA5RO5sRY3CvO9-xqCe1m2CRWLYw'

CASTING_ASSISTANT_TOKEN = 

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1USTJRVEE1TVRZM00wVTVRa0k1TVRJd1JUQkZRVEJEUVRjd05URkVNRVE1UVVVeE1rVTBSQSJ9.eyJpc3MiOiJodHRwczovL3dpc2RvbWlkaS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5OTQ0OWY5N2Q4NzAwYzkxODZiMmVjIiwiYXVkIjoiaWNhc3QiLCJpYXQiOjE1ODc2MDAxMTYsImV4cCI6MTU4NzY4NjUxNiwiYXpwIjoiU1Q2Nkl1bHZYM3ZDbnJMdEpneWd4OW1JS2tuRWtpd1EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.q6OXvs6141QgMkkE3UZmnjDfNo-nzNVQWO4Wy6sTHGSX3-Bg7DXwap1f1fxZE6I5HnSrgt_4y5QM0ijD0RLGqU2dIwOR6oheluE_Z0q8MMutLv-L590V_zGzFBqH45oaMc50_FxbQ-8n3NJ9qU55DnYvYeoCSWF9j_beNZFXVzrWFRLzvQTPEgpmrY-J0Z9QcAKxoqJN_XfrPb6f_gmlVV_zXw5dQ2Kd4VVK2onpghzaTnYkCQtpscdZLYIpeI34ufuCENZsKUijqEaxuEqipY9sC3-coHuQG0T91UHvRfZCBrmUbO9RrwWaTSYvcz13D3dwwiOnaGRGeVmneFG25A'
