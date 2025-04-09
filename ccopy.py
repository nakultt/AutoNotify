import yaml
import xml.etree.ElementTree as ET
from xml.dom import minidom

def append(yaml_file,xml_file):
    try:     
        with open(yaml_file,"r") as yaml_f:
            yaml_data=yaml.safe_load(yaml_f)
        try:
            tree=ET.parse(xml_file)
            root=tree.getroot()
        except FileNotFoundError:
            print("Warning: XML file not found, skipping XML processing.")

        if not isinstance(yaml_data,list):
            yaml_data=[yaml_data]

        for person_data in yaml_data:
            new_person=ET.SubElement(root,"person")
            for key,value in person_data.items():
                if isinstance(value,list):
                    for item in value:
                        child=ET.SubElement(new_person,key)
                        child.text=str(item)
                else:
                    child=ET.SubElement(new_person,key)
                    if value is not None:
                        child.text=str(value)
                    else:
                        child.text=""
        
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
        with open(xml_file,"w") as xml_f:
            xml_f.write(xml_str)

        print(f"Data from {yaml_file} appended to {xml_file} successfully.")
        return True

    except Exception as e:
        print(f"Error appending YAML to XML: {str(e)}")
        return False