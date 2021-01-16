# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
file_path= os.path.join("Resources","netflix_ratings.csv")
find_video=False
# Open the CSV
# when file is open the the object is of type on sigle string i,e when we use open()
# when we read the file whether using open(filename, mode) as file_stream_object and then read the file using read_line or csv reader
#then the new object type is list, where each elelment in the list is the single line in the stream (i.e  line break is used to determin the end of each item in the list)

with open(file_path,"r")  as data_file:
    print(data_file)
    print(type(data_file))
    data_file_lines= csv.reader(data_file,delimiter=',')
    ## the first time file reading object is created it is pointing to the begining of file but not to the first row
    ## the begining of file could have some hexadecimal info related to file or something else.
    print(data_file_lines)
    print(type(data_file_lines))
    #use next function to read first line int he file. 
    data_file_header=next(data_file_lines)
    print(f"{data_file_header}")
    # Loop through looking for the video
    for row in data_file_lines:
        #print (f"{row}")
        #print(type(row))
        if video in row:
            print (row)
            print(type(row))
            find_video=True
            break
    if find_video==False:
        print("Sorry video not found")

    
    