from ..extensions import mongo
from ..models.user import userData
from ..extensions import bcrypt

class UserMongoService:
    def __init__(self):
        self.session = mongo.start_session()
        
    def start_transcation(self):
        self.session.start_transaction()
            
    def commit_transcation(self):
        self.session.commit_transaction()
        
    def abort_transcation(self):
        self.session.abort_transaction()
        
    def get_user(self,id):
        query = {"id": id}
        result = userData.find_one(query)
        return str(result)  
    
    def get_all_names_IDs(self):
        data = userData.find({}, {"id": 1, "name": 1})
        return data
         
    def post_user(self, data):
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8') # hashing the password
        userData.insert_one(data)

    def update_user(self,id ,data):
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
        newUser = {"$set": {"name": data["name"], "email": data["email"] , "password":data["password"]}}
        userData.update_one({"id": id}, newUser)   
        
    def delete_user(self,id) :
        result = userData.delete_one({"id":id})
        return result    
    