# singleton pattern 
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
mongo = MongoClient("mongodb://mongo:27017")
bcrypt = Bcrypt()
