#!/usr/bin/env python3
import csv
import sys

# read data from STDIN and split on each newline
data = sys.stdin.read().splitlines()

# use python's csv library to create a csv reader and a writer
reader = csv.DictReader(data)
writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)

# write the header (first line of the csv)
writer.writeheader()

# loop through the rows in the original csv
for row in reader:
	# filter rows
    if row['PURPOSE'] == 'WATER' and float(row['AMOUNT']) > 1000:
    	# write rows that match above filter
        writer.writerow(row)

#4 make the script executable (chmod +x filter.py)
chmod +x /Development/assignments/filter.py

#5 curl the 2017 quarter 1 expenditure file from
curl -N "https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv" | ./filter.py

#6 redirect the output into a file expensive_water.csv
command > expensive_water.csv

#7 pipe expensive_water.csv into csvstat and redirect that into a file called expensive_water_summary.txt
expensive_water.csv | csvstat

command > expensive_water_summary.txt