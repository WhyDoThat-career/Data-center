from admin import app
from flask import send_from_directory,render_template
from flask import request, redirect, url_for, session
from flask_login import logout_user,current_user
import requests, json

def checkemail():
    email = request.form["email"]
    user = db.session.query(User).filter_by(email=email).first()
    if user is not None and email == user.email :
        print('Exist')
        return "Exist"
    elif user is None and '@' in email :
        if email.split('@')[1] != '' :
            print('No User')
            return "No User"
    else:
        print('Not@')
        return "Not@"

def checkloginpassword():
    email = request.form["email"]
    user = db.session.query(User).filter_by(email=email).first()
    password = request.form["password"]
    if check_password_hash(user.password,password) :
        login_user(user,remember=True, duration=datetime.timedelta(days=30))
        return "correct"
    else:
        return "wrong"

@app.route('/',methods=["GET","POST"])
def index() :
    if request.method == "GET" :
        if not current_user.is_authenticated :
            return redirect(url_for('login'))
        else :
            return redirect('/admin')

@app.route('/checkemail', methods=["POST"])
def check() :
    return checkemail()

@app.route('/login',methods=["GET","POST"])
def login() :
    if request.method == "GET" :
        if not current_user.is_authenticated :
            # return send_from_directory('build','index.html')
            return render_template('login.html')
        else :
            return redirect(url_for('index'))

@app.route('/checkloginpassword', methods=["POST"])
def checkUserpassword():
    return checkloginpassword()

#The admin logout
@app.route('/logout', methods=["GET"])  # URL for logout
def logout():  # logout function
    logout_user()  # remove user session
    return redirect(url_for("login"))  # redirect to home page with message