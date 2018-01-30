import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

pass1="33sidkhore33"

send="khore.sid2@gmail.com"
to="khore.sid2@gmail.com"
sub="email through python "

msg=MIMEMultipart()
msg['From']=send
msg['To']=to
msg['Subject']=sub

body="statment for bank"

msg.attach(MIMEText(body,'plain'))

filename="one.txt"
attachment=open(filename,"rb")

part=MIMEBase("application","octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("content-Disposition","attachment; filename="+filename)

msg.attach(part)

text=msg.as_string()

server=smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(send,pass1)

server.sendmail(send,to,text)
print "sss"
server.quit()




