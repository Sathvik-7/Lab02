from flask import Flask,render_template,request,session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'any'
app.config["MONGO_URI"] = "mongodb://localhost:27017/Week6.UserCredentials"
mongo = PyMongo(app)

@app.route("/")
def base():
    session.pop('attempt', None)
    return render_template('base.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/report",methods=['POST'])
def report():
    temp = 1
    resultSet=[]
    username = request.form['UserName']
    password = request.form['Password']

    if 'attempt' not in session:
        session['attempt'] = 0

    if len(password) < 8:
        temp = 0
        resultSet.append("Your password has less than 8 characters")

    if not any(char.islower() for char in password):
        temp = 0
        resultSet.append("You didnt use lower case letter")

    if not any(char.isupper() for char in password):
        temp = 0
        resultSet.append("You didnt use upper case letter")

    if not password[-1].isdigit():
        temp = 0
        resultSet.append("Your password should end with a number")

    if temp == 1 :
        id = mongo.db.UserCredentials.insert_one({'username':username,'password':password})

    if temp == 0:
        session['attempt'] = session.get('attempt') + 1

    return render_template('report.html', result = resultSet, t = temp , c = session.get('attempt'))

if __name__ == '__main__':
    app.run()
