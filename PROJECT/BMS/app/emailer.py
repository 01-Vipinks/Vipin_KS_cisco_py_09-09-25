"""
Module for sending emails via Gmail SMTP.

Uses credentials defined in mail_config.py.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.mail_config import APP_PASSWORD, FROM_ADDRESS, TO_ADDRESS


def send_gmail(to_addr, subject, body):
    """
    Send an email using Gmail SMTP.

    Args:
        to_addr (str): Recipient email address.
        subject (str): Email subject line.
        body (str): Plain text body of the email.

    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    try:
        msg = MIMEMultipart()
        msg["From"] = FROM_ADDRESS
        msg["To"] = TO_ADDRESS
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(FROM_ADDRESS, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except smtplib.SMTPException as e:
        print("SMTP error:", e)
        return False
    except Exception as e:
        print("Unexpected error:", e)
        return False
