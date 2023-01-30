import csv

with open("EmployeePay.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
