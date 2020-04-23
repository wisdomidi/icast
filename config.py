import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL - DONE
#SQLALCHEMY_DATABASE_URI = "postgres://wisdomidi:Sososoweto2010@localhost:5432/castingdb"
#SQLALCHEMY_DATABASE_URI = "postgres://xqpumnqcsjjpaa:4a81ee23944c334175c4809089519af0a029f6448079f15d66d4be58d433df75@ec2-3-211-48-92.compute-1.amazonaws.com:5432/ddod2t9f2hp648"
SQLALCHEMY_DATABASE_URI = "postgres://ujpfkhwocykutn:2e3a7ecf456796cf946b1d2e71eb58cec6c127909b1fe4e803ce72da09bfcce0@ec2-54-147-209-121.compute-1.amazonaws.com:5432/de7h7cmbl03cua"


SQLALCHEMY_TRACK_MODIFICATIONS = False


#AUTH0_DOMAIN = "wisdomidi.auth0.com"
#JWT_SECRET = "myjwtsecret"
#ClientID = "ST66IulvX3vCnrLtJgygx9mIKknEkiwQ"
#DATABASE_URI = 'postgres://ujpfkhwocykutn:2e3a7ecf456796cf946b1d2e71eb58cec6c127909b1fe4e803ce72da09bfcce0@ec2-54-147-209-121.compute-1.amazonaws.com:5432/de7h7cmbl03cua'