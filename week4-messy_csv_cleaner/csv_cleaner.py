"""
- compute the median value                           DONE
- fill missing age --> median of age                -
- empty embraked --> "s"                            -            
- remove white spaces from every part               -            
- 
"""


"""sort the list --> find midle value --> then assign median value"""

import csv

def find_empty_age(files):
    count = []                        # store ages
    with open(files) as file:         # open file
        reader = csv.reader(file)     # read csv

        for parts in reader:          # loop rows
        
            if parts[0] == "PassengerId": # skip header
                continue

            age = parts[5]            # get age

            if age != "":             # check empty
                count.append(float(age)) # save age

    ascending = sorted(count)         # sort list
    middle = len(ascending)//2        # find middle
    median = ascending[middle]        # value median

    return median                     # return median


def write_clean_data(files, new_files):
    median_age = find_empty_age(files) # get median
    with open(files) as file, open(new_files, "w") as new_file: # open files
        reader = csv.reader(file)     # read old
        writer = csv.writer(new_file) # write new

        for parts in reader:          # loop rows

            if parts[0] == "PassengerId": # write header
                writer.writerow(parts)
                continue

            clean_space = []          # empty list
            for part in parts:        # loop cells
                clean_space.append(part.strip()) # strip text
            parts = clean_space       # update row

            age = parts[5]            # get age
            embark = parts[11]        # get port
            cabin = parts[10]         # get cabin

            if age == "":             # missing age
                parts[5] = str(median_age) # fill median
            
            if embark == "":          # missing port
                parts[11] = "S"       # fill S

            if cabin == "":           # missing cabin
                parts[10] = "Unknown" # fill unknown

            writer.writerow(parts)    # write row


def main():

    input_file = "uncleaned_titanic.csv" # input file
    output_file = "cleaned.csv"       # output file
    write_clean_data(input_file, output_file) # start clean

main()


















