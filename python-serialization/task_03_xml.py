import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        setting = ET.SubElement(root, key)
        setting.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for setting in root:
        result[setting.tag] = setting.text

    return result