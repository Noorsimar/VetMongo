#Flask Web App
import datetime
from flask import *
from MongoDBHelper import MongoDBHelper
import hashlib
from bson.objectid import ObjectId



web_app = Flask("Vets App")


@web_app.route("/")
def index():
    #return "This is Amazing. Its: {}".format(datetime.datetime.today())

    # html_content = """
    # <html>
    #     <title>
    #     Vets App
    #     </title>
    #     <body>
    #         <center>
    #             <h3>
    #             Welcome to Vets App!!
    #             </h3>
    #         </center>
    #     </body>
    # </html>
    # """

    return render_template('index.html')


@web_app.route("/register")
def register():
    return render_template('register.html')

@web_app.route("/home")
def home():
    return render_template('home.html', email=session['vet_email'])

@web_app.route("/register-vet", methods=['POST'])
def register_vet():
    vet_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
        #'password': hashlib.sha256(request.form[''])
        'createdon': datetime.datetime.today()
    }

    print(vet_data)
    db = MongoDBHelper(collections="vets")
    db.insert(vet_data)

    return render_template('home.html', email=session['vet_email'])

@web_app.route("/add-customer", methods=['POST'])
def add_customer():
    customer_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'age': int(request.form['age']),
        'gender': request.form['optradio'],
        'address': request.form['address'],
        'vet_id': session['vet_id'],
        'vet_email': session['vet_email'],
        'createdon': datetime.datetime.today()
    }

    if len(customer_data['name']) == 0 or len(customer_data['phone']) == 0 or len(customer_data['email']) == 0:
        return render_template('error.html', message="Name, Phone and Email cannot be Empty")

    print(customer_data)
    db = MongoDBHelper(collections="customer")
    db.insert(customer_data)

    return render_template('success.html', message="{} added successfully".format(customer_data['name']))




@web_app.route("/login-vet", methods=['POST'])
def login_vet():
    vet_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }

    print(vet_data)
    db = MongoDBHelper(collections="vets")
    # documents = list(db.fetch(vet_data))
    documents = db.fetch(vet_data)

    print(documents, type(documents))
    if len(documents) == 1:
        session['vet_id'] = str(documents[0]['_id'])
        session['vet_email'] = documents[0]['email']
        session['vet_name'] = documents[0]['name']

        print(vars(session))
        return render_template('home.html', email=session['vet_email'], name=session['vet_name'])
    else:
        return render_template('error.html')

@web_app.route("/logout")
def logout():
    session['vet_id'] = ""
    session['email'] = ""
    return redirect("/")

@web_app.route("/fetch-customers")
def fetch_customers_of_vet():
    db = MongoDBHelper(collections="customer")
    # query = {'vet_email': session['vet_email']}
    query = {'vet_id': session['vet_id']}

    documents = db.fetch(query=query)
    print("fetch customers: ", documents, type(documents))

    #return f"Customer Data Fetched for {session['vet_name']}"
    return render_template('customers.html', documents=documents, email=session['vet_email'], name=session['vet_name'])


@web_app.route("/delete-customer/<id>")
def delete_customer(id):
    db = MongoDBHelper(collections="customer")
    query = {'_id': ObjectId(id)}
    db.delete(query)

    return redirect("/fetch-customers")

@web_app.route("/update-customer/<id>")
def update_customer(id):
    db = MongoDBHelper(collections="customer")
    query = {'_id': ObjectId(id)}
    document = db.fetch(query)
    customer = document[0]
    #db.update(document_data_to_update, query)
    return render_template('update-customer.html', customer=customer, email=session['vet_email'], name=session['vet_name'] )

@web_app.route("/update-customer-in-db", methods=['POST'])
def update_customer_in_db():
    update_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'age': int(request.form['age']),
        'gender': request.form['optradio'],
        'address': request.form['address'],
    }

    if len(update_data['name']) == 0 or len(update_data['phone']) == 0 or len(update_data['email']) == 0:
        return render_template('error.html', message="Name, Phone and Email cannot be Empty")

    print(update_data)
    db = MongoDBHelper(collections="customer")
    query = {'email': request.form['email']}
    db.update(update_data, query)

    return render_template('success.html', message="{} Updated Successfully".format(update_data['name']))

@web_app.route("/search", methods=['POST'])
def search():
    print(request.form['to-search'])
    return f"{request.form['to-search']}"


def main():
    #in order to use session object in flask, we need to set some key as secret_key in app
    web_app.secret_key = 'vetsapp-key-1'
    web_app.run(port=5001)

if __name__ == "__main__":
    main()


    #assignmetn Search Customer
    #radio buttons
    #when update, request Id, rather than email- input type="hidden" name"cid" value=customer[_id