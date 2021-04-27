import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader) #it will just pass the first line in the file

    for line in csv_reader:
        print(line) # we can use [0 or 1 or ...] to see specific values
