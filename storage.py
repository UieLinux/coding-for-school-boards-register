from pymongo import MongoClient

__author__ = 'carlozamagni'


class Storage(object):
    def __init__(self, host):
        self.connection = MongoClient(host)

    def get_connection(self):
        return self.connection

    def get_collection(self, db, collection_name):
        return self.connection[db][collection_name]