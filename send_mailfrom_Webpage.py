#!/usr/bin/python
from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
import smtplib
import cgi,cgitb
cgitb.enable()


host = 'smtp.gmail.com'
port = 587
from_email = "jayalipuria@gmail.com"
passwrd = "Radhe_Krishna20"
to_email = "jayalipuria@gmail.com"

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(from_email, passwrd)

the_msg = MIMEMultipart("alternative")
the_msg['Subject'] = "Feedback Form"
the_msg["From"] = from_email
the_msg["To"] = to_email


formData = cgi.FieldStorage()
d={}
d[NAME] = formData.getvalue("NAME")
d[EMAIL] = formData.getvalue("EMAIL")
d[Feedback] = formData.getvalue("Feedback")
for i in d:
    print ("%s: %s"%(i,d[i]))

#part1= MIMEText(html_txt,"html")
#the_msg.attach(part1)

email_conn.sendmail(from_email,to_email,("Feedback from: %s is %s"%(d[NAME],d[Feedback]),"\n Contact by Email: %s"%d[EMAIL]))
email_conn.quit()
