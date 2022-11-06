#CSV Data Parser v1.0
#Author: Hassan Khalil
#Will Output: All Average, Monthly Average, Monthly Max, Monthly Min
#Parses Data from 01-01-2000 till 31-12-2022 regardless of position


#IMPORTS

import csv


#INIT

my_list = []
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


#FUNCTIONS

#find average of all data input O(n)
def find_average_all(array):
    total = 0

    for i in array:
        total += i[1]

    return total / len(array)

#prints average per month O(n)
def monthly_average(array, months):
    total = 0
    year = 22
    month = 12
    operations = 0

    while year > 0:
        while month > 0:
            for i in array:
                if int(i[0][:2]) == month and int(i[0][3:]) == year: #split months and years
                    total += i[1]
                    operations += 1

            if operations != 0: #if month entry exists
                print(f"For Month {months[month]} of Year 20{year}. Average is: {total / operations}")
                total = 0
                operations = 0

            month -= 1 
        year -= 1
        month = 12


#MAIN

#read csv file
with open("./test.csv", 'r') as file:
    csvreader = csv.reader(file) #read file
    for row in csvreader:
        r = row[0].split("\t") #split by \t
        my_list.append(r)
    my_list.pop(0) #remove title

#remove unneccesary day info and convert string data to float
for i, l in enumerate(my_list):
    my_list[i][0] = l[0][3:]
    my_list[i][1] = float(l[1])

print(my_list)
print(find_average_all(my_list))
monthly_average(my_list, months)
