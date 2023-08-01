import datetime

class Customer:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.address = ""
        self.createdon = ""

    def read_customer_data(self):
        self.name = input("Customer Name:").lower()
        self.phone = input("Customer Phone:")
        self.email = input("Customer Email:").lower()
        self.age = int(input("Customer Age:"))
        self.gender = input("Customer Gender(male/female):").lower()
        self.address = input("Customer Address:").lower()
        self.createdon = str(datetime.datetime.today())
        #self.createdon = self.createdon[:self.createdon.rindex(".")]

