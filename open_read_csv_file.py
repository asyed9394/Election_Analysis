# Open the CSV
# when file is open the the object is of type on sigle string i,e when we use open()
# when we read the file whether using open(filename, mode) as file_stream_object and then read the file using read_line or csv reader
#then the new object type is list, where each elelment in the list is the single line in the stream (i.e  line break is used to determin the end of each item in the list)
## the first time file reading object is created it is pointing to the begining of file but not to the first row
## the begining of file could have some hexadecimal info related to file or something else.

import os
import csv

csvpath = os.path.join( 'Resources', 'accounting.csv')

# # Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as file_handler:
     print(file_handler)
     print(type(file_handler))
     print("\n")
     lines = file_handler.read()
     print(f"Using read method {lines}")
     print(type(lines))
     print("\n")

# # Method 1b: Plain Reading of CSV files
with open(csvpath, 'r') as file_handler2:
     print(file_handler2)
     print(type(file_handler2))
     print("\n")
     lines2 = file_handler2.readlines()
     print(f"Using readlines {lines2}")
     print("\n")
# # Method 1c: Plain Reading of CSV files
with open(csvpath, 'r') as file_handler4:
     print(file_handler4)
     print(type(file_handler4))
     print("\n")
     lines4 = file_handler4.readline()
     print(f"Using readline {lines4}")
     print(type(lines4))
     print("\n")
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    print(csvfile)
    print(type(csvfile))
    print("\n")
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    print(type(csvreader))
    print("\n")
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))
    print("\n")
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        print(type(row))
        #print("\n")