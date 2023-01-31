# Import CSV module
import csv


# Create lists and define variables
all_fields = []
fields = []
x = 0


# Read the input CSV file
with open("customers.csv", mode="r") as csv_input:
    reader = csv.reader(csv_input)

    # Add data into the first list
    for row in reader:
        all_fields.append(row)


# Filter data to first name, last name, and country
for row in all_fields:
    row1 = all_fields[x][1]
    row2 = all_fields[x][2]
    row3 = all_fields[x][4]
    fieldrow = [row1, row2, row3]
    fields.append(fieldrow)
    x += 1


# Write the output file
with open("customer_country.csv", "w") as csv_output:
    csvwriter = csv.writer(csv_output)
    for row in fields:
        csvwriter.writerow(row)
