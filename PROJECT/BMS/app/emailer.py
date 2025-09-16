import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.mail_config import app_password, from_address, to_address

def send_gmail(to_address, subject, body):
    # Your Gmail address and App Password are imported above.
    # Make sure to configure app_password, from_address, and to_address in mail_config.py
    
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(from_address, app_password)  # Login with your email credentials
        server.send_message(msg)  # Send the email message
        server.quit()  # Close the connection
        return True
    except Exception as e:
        print("Error:", e)
        return False


# result = send_gmail(to_address, "Account Created Notification", "A new account has been created.")
# print("Mail sent successfully?", result)
