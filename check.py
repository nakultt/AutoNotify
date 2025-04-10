import xml.etree.ElementTree as ET
from datetime import datetime

def check_expiry(xml_file,days_threshold=30):
    near_expiry=[]
    today=datetime.now().date()
    try:
        tree=ET.parse(xml_file)
        root=tree.getroot()

        for person in  root.findall('person'):
            name_element=person.find('name')
            expire_date_element=person.find('expire_date')

            if name_element is not None and expire_date_element is not None and expire_date_element.text is not None:
                name=name_element.text
                try :
                    expire_date=datetime.strptime(expire_date_element.text,"%Y-%m-%d").date()
                    days_left=(expire_date-today).days

                    if 0 < days_left <= days_threshold:
                        near_expiry.append({"name": name ,"expire_date": expire_date_element.text})
                        print(f"Warning: {name}'s expiration date ({expire_date_element.text}) is within {days_left} days.")

                except ValueError:
                    print(f"Invalid expire_date format for {name}: {expire_date_element.text}")

        if not near_expiry:
            print("No expiration dates nearby.")
        return near_expiry
    
    except Exception as e:
        print(f"Error checking expiry: {str(e)}")
        return []