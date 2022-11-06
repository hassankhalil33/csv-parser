import csv

my_dict = []

with open("./test.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        x = row[0].split("\t")
        my_dict.append(x)
    
    my_dict.pop(0)
    print(my_dict)



