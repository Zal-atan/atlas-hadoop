#!/usr/bin/python3
"""takes the output of the mapper.py script and gives the top ten salaries
sorted by totalyearlycompensation."""

import sys

# Initialize an empty list to store the top 10 entries
top_salaries = []

for line in sys.stdin:
    try:
        # Parse the line
        line = line.strip()
        id, rest = line.split("\t")
        company, salary = rest.split(",")
        salary = float(salary)
        
        # Append the new entry
        top_salaries.append((id, salary, company))
        
        # Maintain the list size at a maximum of 10 entries
        top_salaries = sorted(top_salaries, key=lambda x: x[1], reverse=True)[:10]
    
    except ValueError:
        # Skip lines with parsing errors
        continue

# Output the top 10 results in the desired format
for entry in top_salaries:
    id, salary, company = entry
    print(f"{id}\t{salary}\t{company}")
