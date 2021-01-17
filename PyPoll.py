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


#Initialize a total vote counter.
total_votes=0

#Create list variable to hold candidates names
candidate_options =[]

#Create empty dictionary to hold votes and candidate names.
candidate_votes={}

#Variable to track Winning cadidate and winning votes counts and percentage.
winning_candidate=""
winnig_votes=0
winning_percentage=0

with open(file_to_load) as election_data:

    #Read the file object with reader function
    file_reader=csv.reader(election_data)

    #Print the header row
    header=next(file_reader)
    #print(header)
    for row in file_reader:
        #Add the total voites count for each row excluding header
        total_votes +=1

        #Assign the candidtate name from each row, it is third column
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            #Add to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking canadidate votes
            candidate_votes[candidate_name]=0 
            #Increment candidate vots 
        candidate_votes[candidate_name] +=1
#Save the results to our txt file.
with open(file_to_save,"w") as txt_file:
    election_results= (
        f"\nElecton Results\n"
        f"-------------------------\n"
        f"Total Vots: {total_votes:,}\n"
        f"-------------------------\n" )
    print (election_results,end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)

    #Print the total votes
    #print(f"Total votes casted:{total_votes}")
    #Print the candidate list
    #print(candidate_options)
    #print the candidiate votes.
    #print(candidate_votes)

    #Determine the percentage of votes for each candididate by looping throught the candidate vote dictionary
    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage= float(votes)/float(total_votes) * 100
        #print the candidate name and votes percentage
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results=(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
            )
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes>winnig_votes) and (vote_percentage >winning_percentage):
            winnig_votes=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
    #To print out the winning cadidate name , votes and votes percentage to the terminal.
    winning_candidate_summary=(
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winnig_votes:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n")
    print(winning_candidate_summary)
    #Save the winnind candidate summary to text file.
    txt_file.write(winning_candidate_summary)

    
