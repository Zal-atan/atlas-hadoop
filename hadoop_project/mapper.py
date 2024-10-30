#!/usr/bin/python3
"""Module creating the mapper() function"""

import csv
import sys

reader = csv.reader(sys.stdin, delimiter=',')
for row in reader:
    # Check if the row has at least 4 columns
    # if len(row) >= 4:
    try:
        print(f"{row[0]}\t{row[1]},{row[3]}")
    # else:
    except:
        # Handle rows with missing columns, 
        print("Row is missing columns:", row, file=sys.stderr)

