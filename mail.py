from email.mime.base import MIMEBase
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders


user = 'siva.s@masoritherapeutics.com'
password = 'Sivanspeed123$'
smtp = 'smtpout.asia.secureserver.net'
port = 587

def SendMail(to_address, subject, body, attachments):
    sent_from = user

    email_text = """\
    Subject: %s
    %s
    """ % (subject, body)

    message = MIMEMultipart()
    message['From'] = sent_from
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'html'))

    imgCnt = 1
    for attachement in attachments:
        # to add an attachment is just add a MIMEBase object to read a picture locally.
        with open(attachement, 'rb') as f:
            tempfilename = 'img' + str(imgCnt) + '.png'
            # set attachment mime and file name, the image type is png
            mime = MIMEBase('image', 'png', filename=tempfilename)
            # add required header data:
            mime.add_header('Content-Disposition', 'attachment', filename=tempfilename)
            mime.add_header('X-Attachment-Id', '0')
            mime.add_header('Content-ID', '<0>')
            # read attachment file content into the MIMEBase object
            mime.set_payload(f.read())
            # encode with base64
            encoders.encode_base64(mime)
            # add MIMEBase object to MIMEMultipart object
            message.attach(mime)

            imgCnt = imgCnt + 1

    try:
        context = ssl.create_default_context()
        smtp_server = smtplib.SMTP(smtp, port)
        smtp_server.starttls(context=context)
        smtp_server.ehlo()
        smtp_server.login(user, password)
        # smtp_server.sendmail(sent_from, to_address, message.as_string())
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)


def SendMailExcel(to_address, subject, body, attachments):
    sent_from = user

    email_text = """\
    Subject: %s
    %s
    """ % (subject, body)
    print(email_text)

    message = MIMEMultipart()
    message['From'] = sent_from
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'html'))

    imgCnt = 1
    for attachement in attachments:
        # to add an attachment is just add a MIMEBase object to read a picture locally.
        with open(attachement, 'rb') as f:
            tempfilename = 'Export To Excel' + str(imgCnt) + '.xlsx'
            # set attachment mime and file name, the image type is png
            mime = MIMEBase('application', 'octet-stream', filename=tempfilename)
            # add required header data:
            mime.add_header('Content-Disposition', 'attachment', filename=tempfilename)
            mime.add_header('X-Attachment-Id', '0')
            mime.add_header('Content-ID', '<0>')
            # read attachment file content into the MIMEBase object
            mime.set_payload(f.read())
            # encode with base64
            encoders.encode_base64(mime)
            # add MIMEBase object to MIMEMultipart object
            message.attach(mime)

            imgCnt = imgCnt + 1

    try:
        context = ssl.create_default_context()
        smtp_server = smtplib.SMTP(smtp, port)
        smtp_server.starttls(context=context)
        smtp_server.ehlo()
        smtp_server.login(user, password)
        # smtp_server.sendmail(sent_from, to_address, message.as_string())
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)


# import smtplib


# context = ssl.create_default_context()
# smtp_server = smtplib.SMTP('smtpout.secureserver.net', 465)
# smtp_server.starttls(context=context)
# smtp_server.ehlo()

# message = MIMEMultipart()
# message['From'] = 'siva.s@masoritherapeutics.com'
# message['To'] = 'sivaneshmsc@gmail.com'
# message['Subject'] = 'Test mail from masori'

# message.attach(MIMEText('here is the email', 'html'))

# smtp_server.login('siva.s@masoritherapeutics.com', 'Sivanspeed123$')
# smtp_server.sendmail('siva.s@masoritherapeutics.com', 'sivaneshmsc@gmail.com', message.as_string())
# smtp_server.close()
# smtp_server.quit()

# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText

# msg = MIMEMultipart()
# msg.set_unixfrom('author')
# msg['From'] = 'you@mail.com'
# msg['To'] = 'them@mail.com'
# msg['Subject'] = 'simple email in python'
# message = 'here is the email'
# msg.attach(MIMEText(message))

# mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
# mailserver.ehlo()
# mailserver.login('siva.s@masoritherapeutics.com', 'Sivanspeed123$')

# mailserver.sendmail('siva.s@masoritherapeutics.com','sivaneshmsc@gmail.com',msg.as_string())

# mailserver.quit()