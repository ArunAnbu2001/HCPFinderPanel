
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = 'acadiahcpfinder@masori.com'
pwd = "ZN'YP!%Uaawyd&rC"

def SendMail (to_addr, subject, body, attachment):

    try:
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        message = body
        msg.attach(MIMEText(message, "html"))

        mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mailserver.ehlo()
        mailserver.login(from_addr, pwd)
        mailserver.sendmail(from_addr,to_addr,msg.as_string())
        mailserver.quit()
        print ("Email sent successfully!")

    except Exception as ex:
        print ("Something went wrong….", str(ex))
