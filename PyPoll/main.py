import csv
import os
from statistics import mode

budgetdata = os.path.join("Resources", "election_data.csv")

ballotid = []
county = []
candidate = []

# Open and read csv
with open(budgetdata) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

        # adding data to the lists
        ballotid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# finding the average for each candidate and storing them
stockham = candidate.count("Charles Casper Stockham") / len(candidate)
degette = candidate.count("Diana DeGette") / len(candidate)
doane = candidate.count("Raymon Anthony Doane") / len(candidate)

# print results to terminal
print("Election Results")
print("--------------------")
print("Total Votes: " + str(len(ballotid)))
print("--------------------")
print("Charles Casper Stockham: " + str(round(stockham * 100, 3)) + "%" + " (" + str(candidate.count("Charles Casper Stockham")) + ")")
print("Diana DeGette: " + str(round(degette * 100, 3)) + "%" + " (" + str(candidate.count("Diana DeGette")) + ")")
print("Raymon Anthony Doane: " + str(round(doane * 100, 3)) + "%" + " (" + str(candidate.count("Raymon Anthony Doane")) + ")")
print("--------------------")
print("Winner: " + str(mode(candidate)))
print("--------------------")

# print results to electionresults.txt
lines = ["Election Results", 
"--------------------", 
"Total Votes: " + str(len(ballotid)), 
"--------------------", 
"Charles Casper Stockham: " + str(round(stockham * 100, 3)) + "%" + " (" + str(candidate.count("Charles Casper Stockham")) + ")", 
"Diana DeGette: " + str(round(degette * 100, 3)) + "%" + " (" + str(candidate.count("Diana DeGette")) + ")",
"Raymon Anthony Doane: " + str(round(doane * 100, 3)) + "%" + " (" + str(candidate.count("Raymon Anthony Doane")) + ")",
"--------------------",
"Winner: " + str(mode(candidate)),
"--------------------"]
with open('electionresults.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
