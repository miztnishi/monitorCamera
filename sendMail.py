import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.image     import MIMEImage
from datetime import datetime
import message

FROM_ADDRESS = ''
MY_PASSWORD = ''
TO_ADDRESS = ''
BCC = ''
PICTURE = 'picture.png'
SUBJECT = message.getMsg(message.MAIL_SUBJECT, datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
BODY = message.MAIL_BODY


def create_message(from_addr, to_addr, bcc_addrs, subject, body, picture ):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    msg.attach(MIMEText(BODY))

    with open(PICTURE,mode='rb') as p:
        atchment_file = MIMEImage(p.read(),_subtype='png')
        atchment_file.set_param('name', picture)
        atchment_file.add_header('Content-Dispositon','attachment',filename=picture)
        msg.attach(atchment_file)
    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY
    print(subject)
    print(body)

    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body,PICTURE)
    result =  send(FROM_ADDRESS, to_addr, msg)
    print(result)
