import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

def sendMail(to, subject, message, files):
    print("Sending an email to "+to+"...")
    global sender
    global password
    global event
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    for f in files or []:
        with open(f, "rb") as fil:
                msg.attach(MIMEApplication(fil.read(),Content_Disposition='attachment; filename="%s"' % basename(f),Name=basename(f)))


    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(sender, password)
    mailserver.sendmail(sender, to, msg.as_string())
    mailserver.quit()
    print("Succeess.")

sender = input("Email: ")
password = getpass("Password: ")
mails = open(input("Path to file containing the mails: "),"r")
body=open(input("Path to file containing the mail body: "),"r",encoding = "utf-8").read()
cv=input("Path to your cv: ")
for line in mails:
    sendMail(line.strip(),"Application for Internship", body, [cv])