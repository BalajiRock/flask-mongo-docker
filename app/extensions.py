# singleton pattern 
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
mongo = MongoClient("mongodb://localhost:27017")
bcrypt = Bcrypt()
