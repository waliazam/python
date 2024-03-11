import csv
import json

rows = [['Name', 'Age', 'Occupation'],
        ['Jone ', '35 Years', 'Software Engineer'],
        ['Wali', ' 45 Years ', 'Database Administrator']
        ]

with open('output.csv', mode = 'w') as file:
    writer = csv.writer(file)
    writer.writerow(rows)
    
with open('output.json', 'w') as file:
    json.dump(rows, file, indent = 4)