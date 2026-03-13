"""
Titanic Dataset Cleaner

- Strips leading and trailing whitespace from every field in each row.
- Computes the median of available Age values.
- Replaces missing Age values with the computed median.
- Replaces empty Cabin entries with "Unknown".
- Fills missing Embarked values with "S".
- Writes the cleaned dataset to a new CSV file.

"""
import csv

# Collect valid Age values to determine the median
count = []

with open("uncleaned_titanic.csv") as file:
    reader = csv.reader(file)

    for parts in reader:

        if parts[0] == "PassengerId":   # Skip the header row
            continue

        age = parts[5]                  # Access the Age column

        if age == "":                   # Skip rows with missing Age
            continue

        count.append(float(age)) 
        # Append valid age as a float


""" Calculate the median age from the collected numerical values """
ascending = sorted(count)
column    = len(ascending) // 2
median    = ascending[column]


with open("cleaned.csv", "w") as new_file, open("uncleaned_titanic.csv") as file:
    writer = csv.writer(new_file)  # Prepare the writer for the output file
    reader = csv.reader(file)      # Prepare the reader for the input file

    for parts in reader:  

        clean_parts = []
        for part in parts:    # Strip excess whitespace from each cell
            clean_parts.append(part.strip())  
        parts = clean_parts   # Assign the cleaned row back to parts
     
        age    = parts[5]
        embark = parts[11]
        cabin = parts[10]

        if cabin == "":
            parts[10] = "Unknown"

        if embark == "":
            parts[11] = "S"

        if age == "":
            parts[5] = median   

        writer.writerow(parts)
