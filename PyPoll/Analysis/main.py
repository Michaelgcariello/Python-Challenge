# importing modules
import os

import csv

# making path name to csv file
csvpath = os.path.join('.',"PyPoll/Resources/election_data.csv")

# create output file
outputFile = open("electionData.txt",'x')

# opens csv file
with open(csvpath,'r') as csvfile:
    
# making file a variable
    electiondata= (csv.reader(csvfile))

#skip header
    csv_header = next(electiondata)

    electiondata_new=list(electiondata)

filename = open(csvpath,'r')
electiondatalist=csv.DictReader(filename)

#empty lists
ballot_ID=[]
county=[]
candidate=[]

#for loop to count votes
for col in electiondatalist:
    ballot_ID.append(col['Ballot ID'])
    county.append(col['County'])
    candidate.append(col['Candidate'])

#printing results title
print("Election Results")
outputFile.write("Election Results \n")
#printing total votes and value
print("Total Votes:",len(ballot_ID))
outputFile.write(f'Total Votes: {len(ballot_ID)} \n')


#converting candidate list to set to find unique entrys
Unique_Candidate_Names=set(candidate)

#making set of unique candidates a list
Unique_Candidate_Names_list = list(Unique_Candidate_Names)
print(Unique_Candidate_Names_list)
outputFile.write(f'{Unique_Candidate_Names_list} \n')


#count of votes per candidate
candidate1=(candidate.count(Unique_Candidate_Names_list[0]))
candidate2=(candidate.count(Unique_Candidate_Names_list[1]))
candidate3=(candidate.count(Unique_Candidate_Names_list[2]))

#printing candidates, their percent of votes, and total votes
print(Unique_Candidate_Names_list[0],':',candidate1/len(ballot_ID)*100,"%","   Number of Votes:",candidate1)
print(Unique_Candidate_Names_list[1],':',candidate2/len(ballot_ID)*100,"%","   Number of Votes:",candidate2)
print(Unique_Candidate_Names_list[2],':',candidate3/len(ballot_ID)*100,"%","   Number of Votes:",candidate3)
outputFile.write(f'{Unique_Candidate_Names_list[0]} : {candidate1/len(ballot_ID)*100}% Number of Votes:{candidate1} \n')
outputFile.write(f'{Unique_Candidate_Names_list[1]} : {candidate2/len(ballot_ID)*100}% Number of Votes:{candidate2} \n')
outputFile.write(f'{Unique_Candidate_Names_list[2]} : {candidate3/len(ballot_ID)*100}% Number of Votes:{candidate3} \n')

Candidates_Total_Votes = [candidate1,candidate2,candidate3]

# finding the maximum number of votes from the candidates
maximum_vote_total = max(Candidates_Total_Votes)

# determining the position of that maximum value in the list 
position = Candidates_Total_Votes.index(maximum_vote_total)

# knowing this, I can find the corresponding name (aka winner) for the maximum number of votes by using the same position
winner = Unique_Candidate_Names_list[position]
print("Winner:", winner)
outputFile.write(f'Winner : {winner} \n')
outputFile.close()