import pymongo
from tabulate import tabulate

class MongoDBHelper:
    def __init__(self, collections="customer"):
        #uri = "mongodb+srv://<user>:<password>@cluster0.zlyso5w.mongodb.net/?retryWrites=true&w=majority"
        uri = "mongodb+srv://noor:noor@cluster0.zlyso5w.mongodb.net/?retryWrites=true&w=majority"

        client = pymongo.MongoClient(uri)
        self.db = client['groundwork']
        self.collection = self.db[collections]
        print("MongoDB Connected")

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document Inserted: ", result)

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document Deleted: ", result)

    # def fetch(self, query=""):
    #     if len(query) != 0:
    #         document = self.collection.find_one(query)
    #         documents = [document]
    #     else:
    #         documents = self.collection.find()
    def fetch(self, query=""):
        documents = self.collection.find(query)


        # for document in documents:
        #     print(document)
        #print(tabulate(documents, headers="keys", tablefmt="grid"))
        return documents
    def update(self, document, query):
        update_query = {'$set': document} # $set is operator in mongodb
        result = self.collection.update_one(query, update_query)
        print("Updated Document: ", result.modified_count)