import pymongo


class Db:
    URI = "mongodb://localhost:27017"
    DB = None

    @classmethod
    def initialize(cls):
        client = pymongo.MongoClient(cls.URI)
        cls.DB = client['flaskreact']

    @classmethod
    def insert(cls, collection, data):
        cls.DB[collection].insert(data)

    @classmethod
    def find(cls, collection, query):
        return cls.DB[collection].find(query)

    @classmethod
    def find_one(cls, collection, query):
        return cls.DB[collection].find_one(query)
