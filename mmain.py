from ccopy import append
from check import check_expiry
from eemail import send_expiry_alert_email

def main():
    YAML_FILE = "trans.yaml"
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
