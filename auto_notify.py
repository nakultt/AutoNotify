from core.copy_data import append
from core.notify_core import notify_expiry

def main():
    YAML_FILE = "input_data.yaml"
    XML_FILE = "data.xml"
    DAYS_THRESHOLD = 30

    print("Appending YAML data to XML...")
    if not append(YAML_FILE, XML_FILE):
        print("Failed to append data. Exiting.")
        return

    notify_expiry(XML_FILE, DAYS_THRESHOLD)

if __name__ == "__main__":
    main()
