import csv

#Init Variables

my_list = []


#Functions




#Main

#read csv file
with open("./test.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        r = row[0].split("\t")
        my_list.append(r)
    
    my_list.pop(0)


#remove unneccesary day info
for i, l in enumerate(my_list):
    my_list[i][0] = l[0][3:]


print(my_list)