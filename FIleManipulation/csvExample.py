import csv
with open('people.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        print(row)