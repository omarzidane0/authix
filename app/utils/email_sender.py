import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, body):
    EMAIL_ADDRESS = "innovix.offical@gmail.com"
    EMAIL_PASSWORD = "ouxa eany iejq yilq"  
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
