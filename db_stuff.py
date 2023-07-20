from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

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
    guns = None
    all_guns = None

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
        

temp = DB_helper()
