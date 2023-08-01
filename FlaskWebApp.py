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

@web_app.route("/save-vet", methods=['POST'])
def save_vet():
    vet_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd']),
        'createdon': datetime.datetime.today()
    }

    print(vet_data)
    db = MongoDBHelper(collections="vets")
    db.insert(vet_data)

    return "Thankyou!"

def main():
    web_app.run()

if __name__ == "__main__":
    main()