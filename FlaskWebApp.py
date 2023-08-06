#Flask Web App
import datetime
from flask import *
from MongoDBHelper import MongoDBHelper
import hashlib



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

    return render_template('home.html')


@web_app.route("/login-vet", methods=['POST'])
def login_vet():
    vet_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }

    print(vet_data)
    db = MongoDBHelper(collections="vets")
    documents = list(db.fetch(vet_data))
    if len(documents) == 1:
        return render_template('home.html')
    else:
        return render_template('error.html')

def main():
    web_app.run()

if __name__ == "__main__":
    main()