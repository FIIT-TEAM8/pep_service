from pymongo import MongoClient
import api.settings as api_settings

class Database(object):
    DATABASE = None

    # static method, no need to create database object
    @staticmethod
    def initialize():
        # mongo db configuration
        #connection = MongoClient(api_settings.MONGO_SERVER_URL, int(api_settings.MONGO_SERVER_PORT))

        connection = MongoClient(
            host=api_settings.MONGO_SERVER_URL + ":" + str(api_settings.MONGO_SERVER_PORT),
            serverSelectionTimeoutMS = 3000,
            username=api_settings.MONGO_USER,
            password=api_settings.MONGO_PASSWORD
        )

        # connect to ams DB in Mongo
        Database.DATABASE = connection[api_settings.MONGO_DB]

    
    @staticmethod
    def find(collection, to_select):
        return Database.DATABASE[collection].find(to_select)


    @staticmethod
    def find_one(collection, to_select, fields_to_select=False):
        if fields_to_select:
            return Database.DATABASE[collection].find_one(to_select, fields_to_select)
        else:
            return Database.DATABASE[collection].find_one(to_select)