# import libraries
import csv
import os

# path to collect data from csv file

election_data = os.path.join("resources", 'election_data.csv')

# Set the variables

tot_votes = 0
vote_per_cand = 0

# set the arrays

# candidate name

cand_name = []

#  no of vote per candidate in dictionary
Cand_vote = {}

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
     
# identfy the header

    header = next(csvreader)
#print(header)

    for row in csvreader:

        tot_votes = tot_votes + 1

        if row[2] not in cand_name:

            cand_name.append(row[2])

            Cand_vote[row[2]] = 1

        else:
           Cand_vote[row[2]] += 1
    

# print(cand_name)
#print(Cand_vote)


winner = max(Cand_vote, key=Cand_vote.get)

#print(winner)

# format the answers into election analysis report

print("Election Results")
print("-----------------------------")
print(f'Total Votes : {str(tot_votes)}')

print("-----------------------------")

#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php

for candidate, votes in Cand_vote.items():
    print(candidate + " :" + "{:.3%}".format(votes/tot_votes) + " ( " + str(votes) + ")" )

print("-----------------------------")

print(f'Winner : {winner}')

print("-----------------------------")


# Export text files with results

output= open("PyPoll_output.txt", "w") 

output.write("Election Results\n")
output.write("------------------------------------\n")
output.write(f'Total Votes : {str(tot_votes)}\n')
output.write("------------------------------------\n")

for candidate, votes in Cand_vote.items():
    output.write(candidate + " : " + "{:.3%}".format(votes/tot_votes) + " ( " + str(votes) + ")" "\n")

output.write("------------------------------------\n")  

output.write(f'Winner : {winner}\n')
output.write("------------------------------------\n")  