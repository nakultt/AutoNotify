from notify_core import notify_expiry

def main():
    XML_FILE = "data.xml"
    DAYS_THRESHOLD = 30
    notify_expiry(XML_FILE, DAYS_THRESHOLD)

if __name__ == "__main__":
    main()