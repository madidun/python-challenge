import os
import csv

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

#Create variables 
total_votes =  1
list_candidates= 0
votes_percent=0
totalnumberofvotes=0
winner= ""

#Open and read csv file 
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Skip header
    csv_header = next(csvreader)

for row in csvreader:


#Calculate total_votes 
total_votes= sum(votes_percent.values())
print(total_votes)

print("Election Results")
print(f"winner")
print(f"Each candidate’s total votes and percent of votes : {str(votes_percent)}")
print(f"Total votes: {str(total_votes)}")





