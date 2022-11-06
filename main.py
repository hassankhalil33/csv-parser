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

#find average of all data input
def find_average_all(array):
    total = 0

    for i in array:
        total += i[1]

    return total / len(array)

#prints average per month   
def monthly_average(array, months):
    total = 0
    month = 12
    operations = 0

    while month > 0:
        for i in array:
            if int(i[0][:2]) == month:
                total += i[1]
                operations += 1

        if operations != 0:
            print(f"For Month {months[month]}: Average is {total / operations}")
            total = 0
            operations = 0

        month -= 1


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
monthly_average(my_list, months)
