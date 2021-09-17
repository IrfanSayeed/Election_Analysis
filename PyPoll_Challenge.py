# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os


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

# Initialize a total vote counter.
total_votes = 0
total_county_votes=0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list=[]
county_votes={}


# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2:  Track the largest county and county voter turnout.
winning_county=""
winning_county_count=0
winning_county_percentage=0




# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3:  Extract the county name from each row
        county_name=row[1]


        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # 4A:  Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:
       
            # 4B:  Add the existing county to the list of counties. 
            county_list.append(county_name)


            # 4C:  Begin tracking the county's vote count.
            county_votes[county_name] = 0

        if county_name in county_list:

            # 5: Add a vote to that county's vote count.
            county_votes[county_name] += 1
       


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")

    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)


    # 6A:  Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6B:  Retreive the county vote count.
        votes2=county_votes[county_name]

        # 6C:  Calculate the percentage of votes for the county.
        county_vote_percentage=float(votes2)/float(total_votes)*100
        county_results=(
            f"{county_name}: {county_vote_percentage:.1f}% ({votes2:,})\n")

        # 6D:  Print the county results to the terminal.
        print(county_results)


        # 6E:  Save the county votes to the text file.
        txt_file.write(county_results)



        # 6F:  Write an if statement to determine the winning county and get its vote count.
        if (votes2>winning_county_count) and (county_vote_percentage> winning_county_percentage):
            winning_county_count = votes2
            winning_county= county_name
            winning_county_percentage=county_vote_percentage


    # 7:  Print the county with the largest turnout to the terminal.

    winning_county_summary=(
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n"
        #f"Winning County Vote Count:{winning_county_count:,}\n"
        #f"Winning County Percentage: {winning_county_percentage:.1f}%\n"
        )
    print(winning_county_summary)

    # 8:  Save the county with the largest turnout to the text file.
    txt_file.write(winning_county_summary)


    
    # Save the final candidate vote to the text file.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)