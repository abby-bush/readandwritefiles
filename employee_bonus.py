# Import CSV module
import csv


# Read input CSV file
with open("EmployeePay.csv", "r") as csv_input:
    reader = csv.reader(csv_input)

    # Print employee details
    for row in reader:
        print(row)
