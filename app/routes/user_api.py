from flask import Blueprint,request
from ..services.userService import UserService
import json

user = Blueprint('users', __name__, url_prefix='/users')

service = UserService()

@user.route('/', methods=["GET"])
def get_all_users():
    return service.get_all_user_names()

@user.route('/<id>', methods=["GET"])
def get_user(id):
    return service.get_user_data(int(id))

@user.route('/', methods=["POST"])
def post_user():
    data = json.loads(request.data.decode())
    return service.post_user(data)

@user.route('/<id>', methods=["PUT"])
def update_user(id):
    data = json.loads(request.data.decode())
    return service.update_user(int(id), data)

@user.route('/<id>', methods=["DELETE"])
def delete_user(id):
    return service.delete_user(int(id))