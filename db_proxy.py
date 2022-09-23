import os
import mail
import EnDe
import requests
import pandas as pd
#import mysql.connector

from flask import request, session
#from werkzeug.utils import secure_filename

root_path = os.path.dirname(os.path.abspath(__file__))

def register_mail(firstname, lastname, email):
    body = """
    <html>
        <body>
            <p>
                Dear """ + firstname + " " + lastname + """,
            </p>
            <p>
                You have been registered with HCP finder.
            </p>
            <br>
            <p>
                Thanks,
            </p>
            <p>
                <b>Masori Admin Team</b>
            </p>
        </body>
    </html>
    """
    mail.SendMail(email, "You have been Registered - HCP Finder", body, [])
    return


def approve_mail(firstname, lastname, email):
    body = """
    <html>
        <body>
            <p>
                Dear """ + firstname + " " + lastname + """,
            </p>
            <p>
                Your staus have been changed by HCP finder.
            </p>
            <p>
                <b>Staus: </b><b style="color: green;">Approved</b>
            </p>
            <br>
            <p>
                Thanks,
            </p>
            <p>
                <b>Masori Admin Team</b>
            </p>
        </body>
    </html>
    """
    mail.SendMail(email, "Your staus have been changed - HCP Finder", body, [])
    return               
                

def reject_mail(firstname, lastname, email):
    body = """
    <html>
        <body>
            <p>
                Dear """ + firstname + " " + lastname + """,
            </p>
            <p>
                Your staus have been changed by HCP finder.
            </p>
            <p>
                <b>Staus: </b><b style="color: red;">Rejected</b>  
            </p>
            <br>
            <p>
                Thanks,
            </p>
            <p>
                <b>Masori Admin Team</b>
            </p>
        </body>
    </html>
    """
    mail.SendMail(email, "Your staus have been changed - HCP Finder", body, [])
    return       



               


