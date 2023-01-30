import csv

fields = []
fields2 = []

with open("customers.csv", mode="r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        fields.append(row)

x = 0

for row in fields:
    row1 = fields[x][1]
    row2 = fields[x][2]
    row3 = fields[x][4]
    fieldrow = [row1, row2, row3]
    fields2.append(fieldrow)
    x += 1

with open("customer_country.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in fields2:
        csvwriter.writerow(row)
