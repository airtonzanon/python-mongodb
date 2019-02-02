from random import *

class InsertData():

    def __init__(self, db_mongo):
        db_mongo.insert({ "name": "Lord of the rings" + str(randint(1, 100))})
    
