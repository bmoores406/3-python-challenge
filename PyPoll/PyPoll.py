import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    votes = []
    county = []
    canidates = []
    percentage_votes = []
    total_khan = []
    total_correy = []
    total_li = []
    total_otooley = []
    winner = []

    #count of votes
    for row in csvreader: 
           
        votes.append(row[0])
        county.append(row[1])
        canidates.append(row[2])
        total_votes = len(votes)
        print(total_votes)

    #votes per canidate
    for canidate in canidates:
        if canidate =="Khan": khan.append(canidates) 
        khan_votes = len(khan)
        elif canidate =="Correy": correy.append(canidates) 
        correy_votes = len(correy)
        elif canidate =="Li": li.append(canidates)
        li_votes = len(li)
        else: otooley.append(candidates) 
        otooley_votes = len(otooley)

        print(khan_votes)
        print(correy_votes)
        print(li_votes)
        print(otooley_votes)

    #percentages

        percentage_khan = round(((total_kahn/total_votes)*100),2)
        percentage_correy = round(((total_correy/total_votes)*100),2)
        percentage_li = round(((total_li/total_votes)*100),2)
        percentage_otooley = round(((total_otooley/total_votes)*100),2)

        print(percentage_khan)
        print(percentage_correy)
        print(percentage_li)
        print(percentage_otooley)

    #winner
    if percentage_khan > max(percentage_correy, percentage_li, percentage_otooley): winner = "Khan" 
    elif percentage_correy > max(percentage_khan, percentage_li, percentage_otooley): winner = "Correy" 
    elif percentage_li > max(percentage_khan, percentage_correy, percentage_otooley): winner = "Li" 
    elif percentage_otooley > max(percentage_khan, percentage_correy, percentage_li): winner = "O'Tooley"

    #print results
    print("Election Results")
    print(f"-------------------------------------" ) 
    print(f"Total Votes: {str(total_votes)}")
    print(f"-------------------------------------" ) 
    print(f"Khan: {str(percentage_khan)}% ({khan_votes})")
    print(f"Correy: {str(percentage_correy)}% ({correy_votes})")
    print(f"Li: {str(percentage_li)}% ({li_votes})")
    print(f"OTooley: {str(percentage_otooley)}% ({otooley_votes})")
    print(f"-------------------------------------" ) 
    print(f"Winner: {str(winner)}")
    print(f"-------------------------------------" ) 

#with open(output, "w") as poll_results:
with open(file, 'r') as text:
    print (text)
    lines = text.read()
    print(lines)
