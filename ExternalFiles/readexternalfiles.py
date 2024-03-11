import csv

with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)