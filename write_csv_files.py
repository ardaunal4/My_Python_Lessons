import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file: # we create a new csv file with a name of new_names.csv
        csv_writer = csv.writer(new_file, delimiter = '-') #We can discrete content of csv file with dash instead of comma by specifying writer function with delimiter
        # Also there is another posibility to discrete the sections in csv file with tab by specifying the writer func as delimiter = '\t'

    for line in csv_reader:
        csv_writer.writerow(line) # It will write the lines which are in the reader file to the new file

