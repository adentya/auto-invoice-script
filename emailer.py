import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


load_dotenv()

def send_email(invoice_no, month, filename, to, sender_name):
    smtp_server = os.getenv('EMAIL_SMTP_SERVER')
    port = os.getenv('EMAIL_PORT')
    password = os.getenv('EMAIL_PASSWORD')
    sender_email = os.getenv('EMAIL_FROM')
    recipient_email = to
    subject = f'Invoice for {month} {invoice_no}'
    body = f"""
Attached invoice number {invoice_no} for {month}.

Regards,
{sender_name}
"""

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_name
    message['To'] = recipient_email
    message.attach(MIMEText(body, "plain"))

    filepath = f'generated/{filename}'

    with open(filepath, 'rb') as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=ssl.create_default_context())
        server.ehlo()
        server.login(sender_email, password)
        server.send_message(message)
    except Exception as e:
        print(e)
    finally:
        server.quit()


