from xml.etree import ElementTree as ET
from pprint import pprint

xml_file = '../datas/data.xml'

# pprint(open(xml_file).read())

def base_usage():
    tree = ET.parse(xml_file)
    root = tree.getroot()

    facts = root.findall('Fact')
    for fact in facts:
        for items in fact:
            print(items, ':', items.text)
            print('items attr', items.attrib)




base_usage()
