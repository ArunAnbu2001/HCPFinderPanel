import json
from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = 'POC1'

login_users = []
Register_users=[]

@app.route('/home')
def home():
   return render_template('land.html')

@app.route('/profile')
def profile():
   return render_template('profilepage2.html') 

@app.route('/changepassword')
def changepassword():
   return render_template('changepwd.html') 

@app.route('/profile_edit')
def profile_edit():
   return render_template('profileedit.html') 

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register_click')
def register_click():
    return render_template('register1.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    status = ""

    try:
        session["email"] = ''
        status = "updated"
    except:
        pass

    return status
