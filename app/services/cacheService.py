class CacheService:
    def __init__(self, prevData):
        self.cache = dict()
        if prevData != None:
            self.cache = {data["id"]: data["name"] for data in prevData}
    
    def is_user_present(self,id):
        return id in self.cache       
    
    def get_list_of_user_names(self):
        return [self.cache[data] for data in self.cache]
    
    def add_cache(self, id, name):
        self.cache[id] = name
    
    def remove_cache(self, id):
        self.cache.pop(id)    
        
    def update_cache(self, id, name):
        self.cache[id] = name
            