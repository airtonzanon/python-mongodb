from bson.objectid import ObjectId

class MongoClient():

    def __init__(self, client, dbName, collectionName):
        self.db = client[dbName][collectionName]

    def insert(self, data):
        return self.db.insert_one(data).inserted_id
        

    def deleteById(self, id):
        return self.db.delete_one({'_id': ObjectId(id)}).deleted_count

