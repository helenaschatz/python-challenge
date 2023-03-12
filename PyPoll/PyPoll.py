## PyPoll Instructions
#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#Your analysis should look similar to the following:


#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 369711
#  -------------------------
#  Charles Casper Stockham: 23.049% (85213)
#  Diana DeGette: 73.812% (272892)
#  Raymon Anthony Doane: 3.139% (11606)
#  -------------------------
#  Winner: Diana DeGette
#  -------------------------


import os
import csv



# Declare Variables 
total_votes = 0 
charles_votes = 0
diana_votes = 0
raymon_votes = 0



paypoll=os.path.join("Resources","election_data.csv")

# Open csv in default read mode with context manager
with open(paypoll,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)  

     # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham": 
            charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            raymon_votes +=1
        


 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [charles_votes, diana_votes,raymon_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
charles_percent = (charles_votes/total_votes) *100
diana_percent = (diana_votes/total_votes) * 100
raymon_percent = (raymon_votes/total_votes)* 100


# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")


# Output files

Pay_Poll=os.path.join("Resources","Election_Analysis.txt")

with open(Pay_Poll,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
        