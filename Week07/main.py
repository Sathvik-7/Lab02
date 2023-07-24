from flask import Flask,render_template,request,session,redirect,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,LoginManager, login_required,logout_user,current_user
import sqlite3

app = Flask(__name__)
app.secret_key = 'any'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userinfo.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.String(80),nullable=False)
    lastname = db.Column(db.String(80),nullable=False)
    username = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return '<User : %r , firstname : %r,lastname : %r, password : %r>' % (self.username,self.firstname,self.lastname,self.password)

def PasswordValidation(pwd):
    resultSet = []

    if len(pwd) < 8:
        resultSet.append("Your password has less than 8 characters")

    if not any(char.islower() for char in pwd):
        resultSet.append("You didnt use lower case letter")

    if not any(char.isupper() for char in pwd):
        resultSet.append("You didnt use upper case letter")

    if not pwd[-1].isdigit():
        resultSet.append("Your password should end with a number")

    return resultSet

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def main():
    return render_template('SignIn.html')

@app.route("/SignIn",methods=['POST','GET'])
def SignIn():
    success = 0
    r=[]
    if request.method == 'POST':
        un = request.form.get('username')
        pwd = request.form.get('password')
        user = User.query.filter_by(username=un,password=pwd).first()

        if user :
            login_user(user)
            success = 1
            return redirect('/SecretPage')
        else:
            r.append("User name or the password doesnt match")

    return render_template('SignIn.html',result=r)

@app.route("/SignUp",methods=['POST','GET'])
def SignUp():
    success = 0
    r=[]
    if request.method == 'POST':
        fn = request.form.get('firstname')
        ln = request.form.get('lastname')
        un = request.form.get('email')
        pwd = request.form.get('password')
        Cnpwd = request.form.get('Cnpassword')

        if pwd == Cnpwd:
            r = PasswordValidation(pwd)
            user = User.query.filter_by(username=un).first()
            print(user)
            if user :
                r.append("Email already exists try to provide another email")
            else:
                if len(r) == 0:
                    user = User(firstname=fn,lastname=ln,username=un,password=pwd)
                    db.session.add(user)
                    db.session.commit()
                    success = 1
        else:
            r.append("Password and Confirm Password doesnt match")

    if success == 0:
        return render_template('SignUp.html',result=r)
    else:
        return redirect('/Thankyou')

@app.route("/SecretPage")
def SecretPage():
    return render_template('SecretPage.html')

@app.route("/Thankyou")
def Thankyou():
    return render_template('Thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
