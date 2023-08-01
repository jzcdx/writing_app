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
    "date_started": datetime,
    "days_active": integer,
    "last_updated": datetime,
    "goal", integer
}
"""

class DB_helper:
    client = None
    db = None
    persistent_stats = None
    days = None

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
        self.days = self.db.days

    def get_stat(self, stat):
        result = self.persistent_stats.find_one({stat: {"$exists": True}})
        result.pop('_id', None)

        return {stat: result[stat]}

    def set_stat(self, stat):
        result = self.persistent_stats.find_one({stat: {"$exists": True}})

    def upsert_stat(self, stat, value):

        key = {stat : {"$exists": True}}
        item = {stat : value}
        self.persistent_stats.replace_one(key, item, upsert=True);
        print("new stat UPserted." , stat)

    def date_exists(self, date):
        cursor = self.days.find({ "date": date})
        exists = len(list(cursor)) == 1
        
        return exists

    def insert_date(self, date, words):
        key = {"date" : date}
        #item = {"words" : words}
        insert_me = { "date": date, "words" : words }
        self.days.replace_one(key, insert_me, upsert=True);

temp = DB_helper()


print(temp.get_stat("words"));
#temp.upsert_stat("words", 5);
temp.date_exists("2023-7-31")
 
temp.insert_date("2023-07-32", 9999)


"""
TODO:
-create date:word_count archives
-collects the current word count
-update mongo with the current word count for the correspoinding day


-make frontend
displayed stats:
--words/day
--word plus or minus compared to ytd
--graph of previous days and word counts


-find way to run code once a day
"""


#print(temp.get_stat("start_date"));
#print(datetime.now())