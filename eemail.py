import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

#loading .env file
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def send_expiry_alert_email(near_expiry_list):
    if not near_expiry_list:
        print("No email needed: no expiration dates nearby.")
        return True
    if not SENDER_EMAIL or not SENDER_PASSWORD or not RECIPIENT_EMAIL:
        print("Error: Email settings missing!")
        return False
    try:
        subject = "Alert: Nearby Expiration Dates"
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject

        email_body = "The following persons have expiration dates within the next 30 days:\n\n"
        for person in near_expiry_list:
            email_body += f"Name: {person['name']}, Expiration Date: {person['expire_date']}\n"

        msg.attach(MIMEText(email_body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully to {RECIPIENT_EMAIL}!")
        return True

    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False
