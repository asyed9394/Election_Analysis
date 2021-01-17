#Process election results data file and gather following data
#1. Total number of voter casts
#2. A complete list of candiddates who receives vote(s)
#3. The percentage of votes each candidate received
#4. The total number of votes each candidate receieved
#5. The winner of the election based on popular vote

import csv
import os

#Assign a variable to for the file to load and the path.
##file_to_load='Resources\election_results.csv'
file_to_load=os.path.join("Resources","election_results.csv")

#Create a file name variable to direct or indirect path to the file.
file_to_save=os.path.join("Analysis","election_analysis.txt")

#Method1
#election_data=open(file_to_load,'r')
##To do :perform analysis
#election_data.close
#open the election results and read the file.

#Method 2

with open(file_to_load) as election_data:

    #Read the file object with reader function
    file_reader=csv.reader(election_data)

    #Print the header row
    header=next(file_reader)
    print(header)
    for row in file_reader:
        print(row)

    #print the file object
    print(election_data) ## why the print output doesn't match what is in the documentation


#Method 1 to write
#using the open function with w mode we will write data to the file.
#outfile=open(file_to_save,"w")
#write some data to the file
#outfile.write("Hello World")
#outfile.close

#Use with statement to open the file as a text file.

with open(file_to_save,"w") as txt_file:
    
    #write some data to text file
    #txt_file.write("Hello World")

    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jaffesron")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jaffesron, ")
    #txt_file.write("Arapahoe, Denver, Jafferson")
    txt_file.write("Araphoe\nDenver\Jafferson")
