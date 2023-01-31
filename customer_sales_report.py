# Import CSV Module
import csv


# Setting up lists and values
all_fields = []
some_fields = []
fields = [["Customer", "Total"]]
y = 0
x = 0


# Read the input CSV file
with open("sales.csv", "r") as csv_input:
    reader = csv.reader(csv_input)

    # Add values into a list and skip header
    next(reader)
    for i in reader:
        all_fields.append(i)


# Calculate row totals
for row in all_fields:
    row_total = (
        float(all_fields[y][3]) + float(all_fields[y][4]) + float(all_fields[y][5])
    )

    fieldvalues = [all_fields[y][0], row_total]
    y += 1

    some_fields.append(fieldvalues)


# Define original running total value
running_total = some_fields[0][1]


# Calculate customer totals
for row in some_fields:
    if some_fields[x][0] == some_fields[x - 1][0]:
        running_total += some_fields[x][1] + some_fields[x - 1][1]

    else:
        fieldrow = [some_fields[x][0], round(running_total, 2)]
        fields.append(fieldrow)
        running_total = 0

    x += 1


# Write the output CSV file
with open("salesreport.csv", "w") as csv_output:
    writer = csv.writer(csv_output)

    for row in fields:
        writer.writerow(row)
