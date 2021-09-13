# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Add our dependencies
import csv
import os
dir(os)

#Creating a path through the os library
abs_filepath=r"C:\Users\Danielle Spring\Documents\GitHub\Challenges\Election_Analysis\Resources"
script_wd=os.path.dirname(os.path.abspath(__file__))
file_name="election_results.csv"
intermediate="Resources"
file_name_analysis="election_analysis.txt"
intermediate2="analysis"
#Assign a variable to load elections_results file and the path
file_to_load=os.path.join(script_wd,intermediate,file_name)

#Assign a variable to save the analysis file to a path.
file_to_save=os.path.join(script_wd,intermediate2,file_name_analysis)

#1. Initialize a total vote counter.
total_votes= 0

# Candidate options and candidate votes
candidate_options=[]
candidate_votes={}

#Track the winning candidate, vot couunt and percentage
# Declare a variable that holds an empty string value for the winning candidate
winning_candidate=""
# Declare a variable for the "winning count" equal to zero
winning_count=0
#Declare a variable for the "winning_percentage" equal to zero
winning_percentage=0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    #Read the header row.
    headers=next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        
        #Add to the total vote counter.
        total_votes += 1

        #Get the candidate name from each row.
        candidate_name= row[2]

        #If the candidate does not match any existing candidate, add to the candidate list.
        if candidate_name not in candidate_options:
            #Add candidate name to the list of candidates.
            candidate_options.append(candidate_name)
            #And begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name]+=1

#Determine the percentage of votes for each candidate by looping through the counts.
#Interate through the candidate list.
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate.
    votes=candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage=float(votes)/float(total_votes)*100
    #Print out each candidate's name, vote count and percentage of votes to the terminal.
    print(f"{candidate_name}:{vote_percentage:.1f}%({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if the votes are greater than the winning count.
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        #If true then set winning_count =votes and winning_percent=vote_percentage.
        winning_count=votes
        winning_percentage=vote_percentage
        #And, set the winning_candidate equal to the candidate's name.
        winning_candidate=candidate_name

#Print the winning candidate results to the terminal.
winning_candidate_summary=(
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------\n")
print(winning_candidate_summary)


#.......am I saving file here?...............    

    #Save the winning candidate to the text file
    #txt.file.write(winning_candidate_summary)
    
#To do: print out winning candidate's name, vote count, and percentage of votes to the terminal
#print(f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")


#Print the candidate vote dictionary.
#print(candidate_votes)
       
#Print the candidate list.
#print(candidate_options)
        
#3. Print the total votes.
#print(total_votes)

#Using the with statement open the file as a text file.
#with open(file_to_save,"w") as txt_file:
        
        #Write three countries to the analysis file.
        #txt_file.write("Counties in the Election\n-----------------------------\nArapahore\nDenver\nJefferson")
        


#Close the file
election_data.close()
         








