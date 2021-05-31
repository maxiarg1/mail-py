# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import schedule
import shutil
import os 


def mailSender():
 
    # create message object instance
    msg = MIMEMultipart()
     
     
    message = "jads"
     
    # setup the parameters of the message
    password = "flak29fortiger44"
    msg['From'] = "ma@cesetti.com.ar"
    msg['To'] = "ma@cesetti.com.ar"
    msg['Subject'] = "Subscription"
     
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
     
    #create server
    server = smtplib.SMTP('mail.cesetti.com.ar: 587')
     
    server.starttls()
     
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
     
     
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("Sent successfuly...")
    server.quit()
 
#print "successfully sent email to %s:" % (msg['To'])
print("waiting...")
memory = shutil.disk_usage("/")

print(memory)
schedule.every().thursday.at("08:00").do(mailSender)
schedule.every().monday.at("14:39").do(mailSender)


while True:
    schedule.run_pending()

