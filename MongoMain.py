from MongoCustomer import Customer
from MongoDBHelper import MongoDBHelper

def main():
    db = MongoDBHelper()

    # customer = Customer()
    # customer.read_customer_data()
    #
    # document = vars(customer)
    #
    # db.insert(document)

    # query = {'phone': '998706299'}
    # db.delete(query)

    db.fetch()

if __name__ == "__main__":
    main()