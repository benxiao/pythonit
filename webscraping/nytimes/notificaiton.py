import smtplib
from email.message import EmailMessage

SENDER_ADDRESS = "benji.xiao@gmail.com"
SENDER_PASSWORD = "oEp-pQD-X1K-mhl"
RECEIVER_ADDRESS = "ben.xiao@me.com"

def send(subject, text):
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = SENDER_ADDRESS
    msg['To'] = RECEIVER_ADDRESS
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(SENDER_ADDRESS, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
    except:
        pass