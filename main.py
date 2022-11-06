import csv

#INIT

my_list = []


#FUNCTIONS

#find average of all data input
def find_average_all(array):
    total = 0

    for i in array:
        total += i[1]

    return total / len(array)
        

#MAIN

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
print(find_average_all(my_list))
