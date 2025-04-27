from check_date import check_expiry
from email_send import send_expiry_alert_email

def notify_expiry(XML_FILE, DAYS_THRESHOLD):
    print("\nChecking expiration dates...")
    near_expiry_list = check_expiry()

    print("\nSending email if needed...")
    if not send_expiry_alert_email(near_expiry_list):
        print("Failed to send email (if needed).")

        print("\nProcess completed.")
