import csv
import json
import xml.etree.ElementTree as ET

# Writing csv file
rows = [['Name', 'Age', 'Occupation'],
        ['Jone ', '35 Years', 'Software Engineer'],
        ['Wali', ' 45 Years ', 'Database Administrator']
        ]

with open('output.csv', mode = 'w') as file:
    writer = csv.writer(file)
    writer.writerow(rows)
    
#writing json file
    
with open('output.json', 'w') as file:
    json.dump(rows, file, indent = 4)
    
#writing xml file

data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item1.set('name', 'item1')
item1.text = 'item1 description'

tree = ET.ElementTree(data)
tree.write('output.xml')