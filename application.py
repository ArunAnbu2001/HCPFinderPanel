import json
from flask import Flask, render_template, request, session


application = Flask(__name__)
#application.secret_key = 'POC1'

login_users = []
Register_users=[]

@application.route('/home')
def home():
   return render_template('land.html')

@application.route('/profile')
def profile():
   return render_template('profilepage2.html') 

@application.route('/changepassword')
def changepassword():
   return render_template('changepwd.html') 

@application.route('/profile_edit')
def profile_edit():
   return render_template('profileedit.html') 

@application.route('/')
def login():
    return render_template('login.html')

@application.route('/register_click')
def register_click():
    return render_template('register1.html')

@application.route('/logout', methods=['GET', 'POST'])
def logout():
    status = ""

    try:
        session["email"] = ''
        status = "updated"
    except:
        pass

    return status
