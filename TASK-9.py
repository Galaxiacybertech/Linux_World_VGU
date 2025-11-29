import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "nitishkumar098@gmail.com"
APP_PASSWORD = "xewy akvk evkv pbqx"
RECEIVER = "24tec2csic012@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello for python ..."
msg.set_content("This email was shared by Nitish Kumar Gupta.")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)