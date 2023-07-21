from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from datetime import datetime

"""
DB: 
day {
    "words": integer,
    "timestamp": datetime
}

persistent_stats {
    "total_words": integer,
    "date_started": datetime
}
"""

class DB_helper:
    client = None
    persistent_stats = None
    db = None

    def __init__(self):
        self.client = None
        self.connect()

    def test(self):
        print("testing")

    def connect(self):
        print("Connecting to mongodb:")

        username = os.environ['mongo_login']
        password = os.environ['mongo_pw']

        uri = "mongodb+srv://" + username + ":" + password + "@cluster0.7niyeqx.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        #set values to our database and collection
        #self.all_guns = self.client.all_guns #all_guns is the database
        #self.guns = self.all_guns.guns #guns is the collection (basically a table)


        self.db = self.client.story_stats_db #database
        self.persistent_stats = self.db.persistent_stats #collection
        

    def get_stat(self, stat):
        result = self.persistent_stats.find_one({stat: {"$exists": True}})
        result.pop('_id', None)

        return {stat: result[stat]}

    def set_stat(self, stat):
        result = self.persistent_stats.find_one({stat: {"$exists": True}})

    def upsert_stat(self, stat, value):
        #gun_id = self.guns.insert_one(item).inserted_id
        

        key = {stat : {"$exists": True}}
        item = {stat : value}
        self.persistent_stats.replace_one(key, item, upsert=True);
        print("new stat UPserted." , stat)

temp = DB_helper()

print(temp.get_stat("words"));
temp.upsert_stat("words", 5);
#print(temp.get_stat("start_date"));
#print(datetime.now())