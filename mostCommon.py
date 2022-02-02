import csv
holding = []
with open('fives2.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        if len(row[0]) == 5:
            print(len(row[0]))