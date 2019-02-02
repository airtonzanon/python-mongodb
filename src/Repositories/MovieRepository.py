from random import *

class MovieRepository():

    def __init__(self, db_mongo):
        print('insert')
        insertedId = db_mongo.insert({ "name": "Lord of the rings" + str(randint(1, 100))})
        print(insertedId)
        deletedCount = db_mongo.deleteById(insertedId)
        print('deleted: ' + str(deletedCount)) 
