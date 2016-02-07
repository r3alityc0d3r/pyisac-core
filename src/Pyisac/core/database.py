from pymongo import MongoClient

class Database(object):

    def __init__(self, *args, **kwargs):
        init_uri = False

        if len(args) == 1:
            uri = args[0]
            init_uri = True

        if init_uri:
            self.client = client = MongoClient(uri)
        else:
            self.client = client = MongoClient()
        self.db = db = client.pyisac
        self.nodefacts_collection = db.nodefacts_collection
