# all importations
from flask import Flask, render_template
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# initialize app

app = Flask(__name__)

# email variables
port = 2525
smtp_server = 'sandbox.smtp.mailtrap.io'
login = '6ce599b73b2183'
password = '24df6ac777b4bf'
sender_email = 'nyarekigospel@gmail.com'
receiver_email = 'gongoro@kabarak.ac.ke'

# function to send the mail

def send_email(name, phone, email, rooms):
    current_datetime = datetime.now()
    timestamp = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    message = MIMEMultipart("alternative")
    message['Subject'] = ''
    message['From'] = sender_email
    message['To'] = receiver_email

    text = """\
        Hi,
        Here is the information from the new booking:
        name - {}
        phone number - {}
        email - {}
        number of rooms - {}
        time - {}
        """.format(name, phone, email, rooms, timestamp)

    html = render_template('email.html', name=name, phone=phone, email=email, rooms=rooms, timestamp=timestamp)

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP(smtp_server, 2525) as server:
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    
    print('Sent!')

# the route to send the email
@app.route('/')
def home():
    name = 'Mzee Jackson'
    phone = '+254123456789'
    email = 'thisone@gmail.com'
    rooms = '2'
    send_email(name, phone, email, rooms)
    return "ok"

if __name__ == '__main__':
    app.run(port=8111)