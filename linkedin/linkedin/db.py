from linkedin import settings
import pymongo

class MongoDBClient(object):
    def __init__(self, col, index=None):        
        connection = pymongo.Connection(settings.MONGODB_SERVER, settings.MONGODB_PORT)
        self.db = connection[settings.MONGODB_DB]
        self.collection = self.db[col]
        if index:
            self.collection.create_index(index, unique=True)
            
    def get_collection(self):
        return self.collection
    
    def walk(self):
        """
        return all the documents in this collection
        """
        docs = []
        skip = 0
        limit = 1000
        hasMore = True
        while hasMore:
            res = self.collection.find(skip=skip, limit=limit)
            hasMore = (res.count(with_limit_and_skip=True) == limit)
            for x in res:
                docs.append(x)
            skip += limit
        return docs
        
    
