from MongoCustomer import Customer
from MongoDBHelper import MongoDBHelper
from bson.objectid import ObjectId


def main():
    db = MongoDBHelper()

    # customer = Customer()
    # customer.read_customer_data()
    #
    # document = vars(customer)
    #
    # db.insert(document)

    # query = {'phone': '998706299', 'age':21}
    #query = {'phone': '987654321'}
    #query = {"_id": ObjectId("64c8ff61691fdd034ae16537")}
    query = {'email': 'nooi@noori.com'}
    # db.delete(query)

    #db.fetch()
    db.fetch(query=query)

    document_data_to_update = {'name': 'noori', 'age': 33, 'email':'noori@noori.com'}
    db.update(document_data_to_update, query)


if __name__ == "__main__":
    main()