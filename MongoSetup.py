import pymongo

uri = "mongodb+srv://<>:<>@cluster0.zlyso5w.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)

db = client['groundwork']

collections = db.list_collection_names()

print(collections)

for collection in collections:
    print(collection)
