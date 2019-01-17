import os
import csv

csvpath = "/Users/MG/Desktop/election_data.csv"

out_file = "/Users/MG/Desktop/Py Poll.txt"

vote_total = 0
vote_candidates = {}
list_candidates = []
winning_count = 0
winning_candidates = ""


with open(csvpath) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
    
    
    for row in reader: 

        print(".", end=""),
    
#The total number of votes cast

        vote_total = vote_total + 1


#A complete list of candidates who received votes

        name_candidates = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if name_candidates not in list_candidates:

            # Add it to the list of candidates in the running
            list_candidates.append(name_candidates)

            # And begin tracking that candidate's voter count
            vote_candidates[name_candidates] = 0

        # Then add a vote to that candidate's count
        vote_candidates[name_candidates] = vote_candidates[name_candidates] + 1

with open(out_file, "w") as txt_file:

    election_results = (
        f"n\nElection Results\n"
        f"-----------------------------------------\n"
        f"Total Votes: {vote_total}\n"
        f"-----------------------------------------\n")
    print(election_results, end="")
#Loop through the counts

    for candidate in vote_candidates:

#The percentage of votes each candidate won
        
        votes = vote_candidates.get(candidate)
        vote_percentage = float(votes) / float(vote_total) * 100

#The winner of the election based on popular vote.

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
    
            
winning_candidate_summary = (
       f"-----------------------------------------\n"
       f"Winner: {winning_candidate}\n")

print(winning_candidate_summary, end="")
