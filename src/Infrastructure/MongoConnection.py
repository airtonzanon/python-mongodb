class MongoConnection():

    def __init__(self, client):
        self.client = client

    def insert(self, data):
        xuplauDatabase = self.client.xuplau
        xuplauDatabase.movies.insert(data)

