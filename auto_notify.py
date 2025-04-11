from copy_data import append
from check_date import check_expiry
from email_send import send_expiry_alert_email

def main():
    YAML_FILE = "input_data.yaml"
    XML_FILE = "data.xml"
    DAYS_THRESHOLD = 30

    print("Appending YAML data to XML...")
    if not append(YAML_FILE, XML_FILE):
        print("Failed to append data. Exiting.")
        return

    print("\nChecking expiration dates...")
    near_expiry_list = check_expiry(XML_FILE, DAYS_THRESHOLD)

    print("\nSending email if needed...")
    if not send_expiry_alert_email(near_expiry_list):
        print("Failed to send email (if needed).")

        print("\nProcess completed.")

if __name__ == "__main__":
    main()
