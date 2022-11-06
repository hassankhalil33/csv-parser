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


#remove unneccesary day info and convert string data to float
for i, l in enumerate(my_list):
    my_list[i][0] = l[0][3:]
    my_list[i][1] = float(l[1])


print(my_list)
