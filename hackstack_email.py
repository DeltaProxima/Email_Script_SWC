import smtplib
import pathlib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.base import MIMEBase
import os

import codecs

dct={
    "HTML/CSS/JS":"https://chat.whatsapp.com/IfY5MAPeeVW86FXnfA5qr6",
    "Node.js": "https://chat.whatsapp.com/DerBTSNziMaBUEAiK9oYWl",
    "React": "https://chat.whatsapp.com/BvDBfYPmYeL22axPtxNTJB",
    "Flutter": "https://chat.whatsapp.com/GrFHPxfOIPn6FV54L2UoAq",
    "UI/UX":"https://chat.whatsapp.com/DspVEKiydxwAXYy3hGya7S"
}

def send_email(name, workshops,dct,server,from_mail,to_mail):
    dir = pathlib.Path(__file__).parent.absolute()
    path_plot = str(dir) + '\header.png'
    msg = MIMEMultipart()
    msg['Subject'] = 'HackStack 2023 Workshop WhatsApp Group Link'
    msg['From'] = from_mail
    COMMASPACE = ', '
    msg['To'] = COMMASPACE.join([from_mail, to_mail])
    msg.preamble = 'HackStack 2023 Workshop WhatsApp Group Link'
    print(path_plot)
    with open(path_plot, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename='header.png')
        img.add_header('X-Attachment-Id', '0')
        img.add_header('Content-ID', '<0>')
        fp.close()
    f = codecs.open(str(dir) + "/email.html", 'r')
    string = f.read()
    links ="<ol>"
    wnames=''
    for i in workshops:
        wshp = "<li>"+ i +" : " + "<a href=\""+dct[i]+ "\">"+dct[i]+"</a></li>"
        wnames+= " , " + i
        links+=wshp
    links+="</ol>"
    # Replace the relative path to images with ContentID
    html_string = string.replace("Everyone", name)
    html_string = string.replace("./header.png", "cid:0")
    html_string = string.replace("A,B,C,D", wnames)
    html_string = html_string.replace("Insert Links Here", links)
    msg.attach(MIMEText(html_string, 'html', 'utf-8'))
    server.sendmail(from_mail, to_mail, msg.as_string())
smtp_server="smtp.office365.com"
from_mail = "swc@iitg.ac.in"
from_password = "Rahul@123"
to_mail="d.vighnesh@iitg.ac.in"
smtp_port=587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.ehlo()
server.login(from_mail, from_password)
name="Vighnesh Deshpande"
workshops=["HTML/CSS/JS","Flutter"]
send_email(name, workshops,dct,server,from_mail,to_mail)
server.quit()
