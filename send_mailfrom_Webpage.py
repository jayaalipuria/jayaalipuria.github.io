#!C:\Python34\python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import cgi,cgitb
cgitb.enable()

print ("Content-Type: text/html\n\n")

formData = cgi.FieldStorage()
d={}
d[NAME] = formData.getvalue("NAME")
d[EMAIL] = formData.getvalue("EMAIL")
d[Feedback] = formData.getvalue("Feedback")
for i in d:
    print ("%s: %s"%(i,d[i]))
    
from_email = "jayalipuria@gmail.com"
passwrd = "Radhe_Krishna20"
to_email = "jayalipuria@gmail.com"


the_msg = MIMEMultipart("alternative")
the_msg['Subject'] = "Feedback Form"
the_msg["From"] = from_email
the_msg["To"] = to_email

body="('Hi, A feedback mail from %s is received./n Feedback:%s/n/n Thanks and regards/n Contact Mail:%s'%(d[NAME],d[Feedback],d[EMAIL]))"
part1= MIMEText(body,"plain")
the_msg.attach(part1)

host = 'localhost'
#port = 80
email_conn = smtplib.SMTP(host)
email_conn.set_debuglevel(1)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(from_email, passwrd)
email_conn.sendmail(from_email,to_email,the_msg.as_string())
email_conn.quit()
