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
print(file_to_load)
#Assign a variable to save the analysis file to a path.
file_to_save=os.path.join(script_wd,intermediate2,file_name_analysis)

#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    #Print the header row.
    headers=next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    #for row in file_reader:
        #print(row)


#Using the with statement open the file as a text file.
with open(file_to_save,"w") as txt_file:
        
        #Write three countries to the analysis file.
        txt_file.write("Counties in the Election\n-----------------------------\nArapahore\nDenver\nJefferson")
        


#Close the file
election_data.close()
         








