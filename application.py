
import db_proxy
import json
from flask import Flask, render_template, request, session


application = Flask(__name__)
application.secret_key = 'POC1'

login_users = []
Register_users=[]

@application.route('/home')
def home():
    try:
        if session["email"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
    
    return render_template('land.html')

@application.route('/profile')
def profile():
    try:
        if session["email"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
    
    return render_template('profilepage2.html') 

@application.route('/changepassword')
def changepassword():
    try:
        if session["email"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
    
    return render_template('changepwd.html') 

@application.route('/profile_edit')
def profile_edit():
    try:
        if session["email"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
    
    return render_template('profileedit.html') 

@application.route('/')
def login():
    return render_template('login.html')

@application.route('/register_click')
def register_click():
    try:
        if session["email"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
    
    return render_template('register1.html')

@application.route('/doctor_details')
def doctor_details():
    try:
        if session["email"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
    
    return render_template('doctor_details.html')
   
@application.route('/dashboard')
def dashboard():
    try:
        if session["email"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
    
    return render_template('dashboard.html')

@application.route('/logon', methods=['POST'])
def logon():
    res = False
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
      
        session["email"] = email

        res, usertype, username = db_proxy.check_user(email, password)
        session['UserType'] = usertype
        session['UserName'] = username

        if res == True:
            login_users.append(email)
            session["email"] = email

    return json.dumps(res)


@application.route("/get_register_table" ,methods=["GET","POST"])
def get_register_table():
    intent=db_proxy.get_register_table()
    return intent.to_json(orient="index")

@application.route("/partial_load" ,methods=["GET","POST"])
def partial_load():
    intent=db_proxy.get_pagination_data()
    return json.dumps(intent, default=str)

@application.route('/bulk_upload', methods=['GET', 'POST'])
def bulk_upload():
    intent=db_proxy.bulk_upload()
    return json.dumps(intent)

@application.route('/reject_doctor', methods=['GET', 'POST'])
def reject_doctor():
    intent=db_proxy.reject_doctor()
    return json.dumps(intent)

@application.route('/reject_reason_doctor', methods=['GET', 'POST'])
def reject_reason_doctor():
    intent=db_proxy.reject_reason_doctor()
    return json.dumps(intent)

@application.route('/approve_doctor', methods=['GET', 'POST'])
def approve_doctor():
    intent=db_proxy.approve_doctor()
    return json.dumps(intent)

@application.route('/pending_doctor', methods=['GET', 'POST'])
def pending_doctor():
    intent=db_proxy.pending_doctor()
    return json.dumps(intent)

@application.route('/delete_doctor', methods=['GET', 'POST'])
def delete_doctor():
    intent=db_proxy.delete_doctor()
    return json.dumps(intent)

@application.route('/update_data', methods=['POST'])
def update_data():
    res = db_proxy.update_data()
    return json.dumps(res)

@application.route('/register', methods=['POST'])
def register():  
    res = db_proxy.register()
    return json.dumps(res)

@application.route('/change_password', methods=['POST'])
def change_password():
    res = db_proxy.change_password()
    return json.dumps(res)

@application.route('/update_profile', methods=['POST'])
def update_profile():
    res = db_proxy.update_profile()
    return json.dumps(res)

@application.route('/fetch', methods=['GET'])
def fetch():
    res = db_proxy.fetch()
    return json.dumps(res)

@application.route('/optout')
def optout():  
   return render_template('optout.html')
   
@application.route('/fetch_opt', methods=['POST'])
def fetch_opt():
    if request.method == 'POST':
        Npinumber=request.form['Npi']
        res = db_proxy.fetch_opt(Npinumber)
        return json.dumps(res)

@application.route('/update_opt', methods=['POST'])
def update_opt():
    res = db_proxy.update_opt()
    return json.dumps(res)

@application.route('/get_gmkey', methods=['POST'])
def get_gmkey():
    res = db_proxy.get_gmkey()
    return json.dumps(res)
    
@application.route('/logout', methods=['GET', 'POST'])
def logout():
    status = ""

    try:
        session["email"] = ''
        status = "updated"
    except:
        pass

    return status

@application.route('/get_dashboard_data', methods=['GET', 'POST'])
def get_dashboard_data():
    res = db_proxy.get_dashboard_data()
    return json.dumps(res)
