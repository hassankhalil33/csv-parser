#CSV Data Parser v1.0
#Author: Hassan Khalil
#Will Output: All Average, Monthly Average, Monthly Maximum, Monthly Minimum
#Parses Data from 01-01-2000 till 31-12-2022 regardless of order
#Data MUST Match Example CSV


#IMPORTS

import csv


#INIT

address = ""
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

#read csv file
def read_file(address):
    array = []

    with open(address, 'r') as file:
        csvreader = csv.reader(file) #read file
        for row in csvreader:
            array.append(row)
        array.pop(0) #remove title

    return array

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

#prints maximum value per month O(n)
def monthly_maximum(array, months):
    maximum = 0
    year = 22
    month = 12
    operations = 0

    while year > 0:
        while month > 0:
            for i in array:
                if int(i[0][:2]) == month and int(i[0][3:]) == year: #split months and years
                    if i[1] > maximum:
                        maximum = i[1]
                        operations += 1
                
            if operations != 0: #if month entry exists
                print(f"For Month {months[month]} of Year 20{year}. Maximum is: {maximum}")
                maximum = 0
                operations = 0

            month -= 1 
        year -= 1
        month = 12

#prints minimum value per month O(n)
def monthly_minimum(array, months):
    minimum = 0
    year = 22
    month = 12
    operations = 0

    while year > 0:
        while month > 0:
            for i in array:
                if int(i[0][:2]) == month and int(i[0][3:]) == year: #split months and years
                    if minimum == 0: #save the first number 
                        minimum = i[1]

                    elif i[1] < minimum:
                        minimum = i[1]
                        operations += 1
                
            if operations != 0: #if month entry exists
                print(f"For Month {months[month]} of Year 20{year}. Minimum is: {minimum}")
                minimum = 0
                operations = 0

            month -= 1 
        year -= 1
        month = 12


#MAIN

#input address
print("Welcome to CSV Data Parser v1.0")
address = input("Please input address of .csv file: ")
my_list = read_file(address)

#check if empty data
if len(my_list) < 2:
    raise Exception("Invalid Address or Empty CSV File!")

print(my_list)

#remove unneccesary date/value title and convert string data to float
for i, l in enumerate(my_list):
    my_list[i][0] = l[0][3:]
    my_list[i][1] = float(l[1])

#print data
print(f"Total Average is: {find_average_all(my_list)}")
monthly_average(my_list, months)
monthly_maximum(my_list, months)
monthly_minimum(my_list, months)
