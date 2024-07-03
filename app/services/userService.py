from .cacheService import CacheService
from .userMongoService import UserMongoService
import json 

class UserService:
    def __init__(self):
        self.userMongoService = UserMongoService()
        data = self.userMongoService.get_all_names_IDs()
        self.cacheService = CacheService(data)
        
    def get_all_user_names(self):
        listOfAllusers = self.cacheService.get_list_of_user_names()
        return json.dumps({"userNames":listOfAllusers})

    def get_user_data(self, id):
        if self.cacheService.is_user_present(id):
            result = self.userMongoService.get_user(id)
            return json.dumps(result), 200
        else:
            return json.dumps({"error": "User not found."}), 404   

    def post_user(self, data):
        self.userMongoService.start_transcation()
        if self.cacheService.is_user_present(int(data["id"])):
            self.userMongoService.abort_transcation()
            return json.dumps({"error": "User id already exist."}), 409
        else:
            self.userMongoService.post_user(data)
            self.cacheService.add_cache(data["id"],data["name"])
            self.userMongoService.commit_transcation()
            return json.dumps({"message": "Data posted"}), 200         
        
    def update_user(self, id, data):
        self.userMongoService.start_transcation()
        if self.cacheService.is_user_present(id):
            self.userMongoService.update_user(id, data)
            self.cacheService.update_cache(data["id"], data["name"])
            self.userMongoService.commit_transcation()
            return json.dumps({"message": "Data updated"}), 200
        else:
            self.userMongoService.abort_transcation()
            return json.dumps({"error": "User not found."}), 404      
        
    def delete_user(self, id):
        self.userMongoService.start_transcation()
        if self.cacheService.is_user_present(id):
            self.userMongoService.delete_user(id)
            self.cacheService.remove_cache(id)
            self.userMongoService.commit_transcation()
            return json.dumps({"message": "User deleted successfully."}), 200
        else:
            self.userMongoService.abort_transcation()
            return json.dumps({"error": "User not found."}), 404                                          