from flask import Blueprint,request
from ..extensions import mongo
from ..extensions import bcrypt
from ..models.user import userData
import json 
user = Blueprint('users', __name__, url_prefix='/users')
# caching to improve performance
# Store the previous data 
prevData = userData.find({}, {"id": 1, "name": 1})
cache = {data["id"]: data["name"] for data in prevData} # cache the user IDs and Names in dictionary for constant time

# return userIDs from the cache
@user.route('/', methods=["GET"])
def get_all_users():
    allUsersnames = [cache[data] for data in cache]
    print(allUsersnames)
    return json.dumps({"userNames":allUsersnames})


@user.route('/<id>', methods=["GET"])
def get_user(id):
    id = int(id)
    print(type(id))
    # check if the user exists 
    if id not in cache.keys():
        return json.dumps({"error": f"User not found."}), 404
    else:
        query = {"id": id}
        result = userData.find_one(query)
        result['_id'] = str(result['_id'])
        return json.dumps(result), 200


@user.route('/', methods=["POST"])
def post_user():
    session = mongo.start_session()
    session.start_transaction()
    try:
        data = json.loads(request.data.decode())
        # find all the users in cache and check if id exists
        if data["id"] in cache.keys():
            session.abort_transaction()
            session.end_session()
            return json.dumps({"error": "User id already exist."}), 409
        # assuming the data validation is done in frontend we directly insert the data 
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8') # hashing the password
        userData.insert_one(data)
        cache[data["id"]] = data["name"]
        print(cache)
        session.commit_transaction()
        session.end_session()
        return json.dumps({"message": "Data posted"}), 200
    except Exception as e:
        session.abort_transaction()
        session.end_session()
        return json.dumps({"error": str(e)}), 500

@user.route('/<id>', methods=["PUT"])
def update_user(id):
    id = int(id)
    session = mongo.start_session()
    session.start_transaction()
    try:
        data = json.loads(request.data.decode())
        if id not in cache.keys():
            session.abort_transaction()
            session.end_session()
            return json.dumps({"error": f"User id not found."}), 404
        
        #updated user 
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
        new_user = {"$set": {"name": data["name"], "email": data["email"] , "password":data["password"]}}
        userData.update_one({"id": id}, new_user)
        cache[id] = data["name"]
        session.commit_transaction()
        session.end_session()
            
        return json.dumps({"message": "Data updated"}), 200
    except Exception as e:
        session.abort_transaction()
        session.end_session()
        return json.dumps({"error": str(e)}), 500
        

@user.route('/<id>', methods=["DELETE"])
def delete_user(id):
    id = int(id)
    session = mongo.start_session()
    session.start_transaction()
    try:
        result = userData.delete_one({"id":id})
        cache.pop(id)
        if result.deleted_count == 1: # deleted user
            session.commit_transaction()
            session.end_session()
            return json.dumps({"message": "User deleted successfully."}), 200
        else: # not deleted
            session.abort_transaction()
            session.end_session()
            return json.dumps({"error": "User Id not found."}), 404
    except Exception as e:
        session.abort_transaction()
        session.end_session()
        return json.dumps({"error": str(e)}), 500