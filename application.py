import db_proxy
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

@app.route('/logon', methods=['POST'])
def logon():
    res = False
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        res, usertype, username = db_proxy.check_user(email, password)
        print(usertype)
        session['UserType'] = usertype
        session['UserName'] = username

        if res == True:
            login_users.append(email)
            session["email"] = email

    return json.dumps(res)


@app.route("/get_register_table" ,methods=["GET","POST"])
def get_register_table():
    intent=db_proxy.get_register_table()
    return intent.to_json(orient="index")

@app.route('/bulk_upload', methods=['GET', 'POST'])
def bulk_upload():
    intent=db_proxy.bulk_upload()
    return json.dumps(intent)

@app.route('/reject_doctor', methods=['GET', 'POST'])
def reject_doctor():
    intent=db_proxy.reject_doctor()
    return json.dumps(intent)

@app.route('/reject_reason_doctor', methods=['GET', 'POST'])
def reject_reason_doctor():
    intent=db_proxy.reject_reason_doctor()
    return json.dumps(intent)

@app.route('/approve_doctor', methods=['GET', 'POST'])
def approve_doctor():
    intent=db_proxy.approve_doctor()
    return json.dumps(intent)

@app.route('/pending_doctor', methods=['GET', 'POST'])
def pending_doctor():
    intent=db_proxy.pending_doctor()
    return json.dumps(intent)

@app.route('/delete_doctor', methods=['GET', 'POST'])
def delete_doctor():
    intent=db_proxy.delete_doctor()
    return json.dumps(intent)

@app.route('/update_data', methods=['POST'])
def update_data():
    res = db_proxy.update_data()
    return json.dumps(res)

@app.route('/register', methods=['POST'])
def register():  
    res = db_proxy.register()
    return json.dumps(res)

@app.route('/change_password', methods=['POST'])
def change_password():
    res = db_proxy.change_password()
    return json.dumps(res)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    res = db_proxy.update_profile()
    return json.dumps(res)

@app.route('/fetch', methods=['GET'])
def fetch():
    res = db_proxy.fetch()
    return json.dumps(res)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    status = ""

    try:
        session["email"] = ''
        status = "updated"
    except:
        pass

    return status
