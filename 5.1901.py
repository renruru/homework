import csv

with open('./date.csv') as csvFile:
    dates = csv.reader(csvFile)
    for x in dates:
        print(x)