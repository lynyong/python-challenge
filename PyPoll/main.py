# Modules
import os 
import csv 

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header 
    csv_header = next(csvreader)

    # Set variables 
    total_votes = 0
    vote_table = {} 
    winner = "x" 
    highest_vote = 0
    
    # Loop through csv
    for row in csvreader:

    # The total number of votes cast
        total_votes = total_votes + 1

    # A complete list of candidates who received votes
        candidate = row[2]
        if candidate in vote_table:
            vote_table[candidate] = vote_table[candidate] + 1
        else :
            vote_table[candidate] = 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

# The percentage of vote and total number of votes each candidate won, and the winner of the election based on popular vote
for key in vote_table:
    print(key + ": " + format(vote_table[key]/total_votes*100, ".3f") + "% " + "(" + str(vote_table[key]) + ")")
    if int(vote_table[key]) > int(highest_vote):
        highest_vote = vote_table[key]
        winner = key
print("-------------------------")
print("Winner : " + winner)
print("-------------------------")

# Specify the file to write to
analysis_path = os.path.join("analysis", "analysis.txt")

# Open the analysis file using "write" mode, and then write the analysis to the .txt
with open(analysis_path, 'w') as txtfile:
    txtfile.write ("Election Results\n") 
    txtfile.write ("-------------------------\n")
    txtfile.write ("Total Votes: " + str(total_votes) + "\n")
    txtfile.write ("-------------------------\n")
    for key in vote_table:
        txtfile.write(key + ": " + format(vote_table[key]/total_votes*100, ".3f") + "% " + "(" + str(vote_table[key]) + ")" + "\n")
    txtfile.write ("-------------------------\n")    
    txtfile.write ("Winner : " + winner + "\n")
    txtfile.write ("-------------------------\n")