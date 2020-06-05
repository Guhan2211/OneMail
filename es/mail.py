import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from string import Template
def m_wt_attach(name,email,attachment):
    #Enter you body text here---------------------------
    mail_content = '''Hello {} ,
    This is a test mail.
    In this mail we are sending some attachments.
    The mail is sent using Python SMTP library.
    Thank You
    '''.format(name)
    #print(mail_content)   
    sender_address = 'onemail@techvile.in'
    sender_pass = 'Onemail@123'
    receiver_address = email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address

    #-------------------Enter Your Subject here----------------
    message['Subject'] = 'Test try!'
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = attachment
    #print(attach_file_name)
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'pdf',Name="{}.pdf".format(name))
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename="{}.pdf".format(name))
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.hostinger.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent to {}'.format(name))


def m_wtout_attach(rcvrs,sub,body):

    for rcv in rcvrs:
        MY_ADDRESS="onemail@techvile.in"
        s = smtplib.SMTP(host='smtp.hostinger.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, "Onemail@123")
        #${PERSON_NAME}
        msg = MIMEMultipart()    
        Name=["tester1"]  
        message=Template(body)
  
        message = message.substitute(PERSON_NAME=Name[0])
        #print(message)
        #message=body
        msg['From']=MY_ADDRESS
        msg['To']=rcv
        msg['Subject']=sub
        msg.attach(MIMEText(message, 'html'))
        s.send_message(msg)
        s.quit()
    print("Sent request complete")