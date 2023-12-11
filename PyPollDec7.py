import os
import csv

#open the file, name the output
election_data_csv = os.path.join("Resources","election_data.csv")
output_file=os.path.join("Analysis", "results.txt")

#declare variables
total_votes = 0
list_of_candidates = []
candidates={}
winning_candidate=""
winning_count=0

# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

#track the total months and profit
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    #loop through each row in the csvreader; add the votes
    for row in csvreader:

    #add to the total vote count
        total_votes += 1

    #get candidate name from each row and if not there, add to the candidate list
        candidate_name=row[2]
        if candidate_name not in list_of_candidates:
            list_of_candidates.append(candidate_name)
            candidates[candidate_name]=0
        #sets name to the dictionary while adding the votes    
        candidates[candidate_name] += 1

#tell it how and where to display results
with open(output_file,"w") as txt_file:
    election_total=f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------

'''
    print(election_total)
    txt_file.write(election_total)

#find the votes for each candidate
    for candidate in candidates:
        votes=candidates.get(candidate)
        vote_percentage=float(votes)/float(total_votes)*100

#look for winning candidtae
        if votes > winning_count:
            winning_count= votes
            winning_candidate=candidate


#declare variable to show the candidate results
        candidate_results=f"{candidate}:{vote_percentage:.3f}% ({votes:,})\n"
    
    #print & save results
        print(candidate_results)
        txt_file.write(candidate_results)
   
   #print results and send to file

    winning_candidate_results=f'''
--------------------------
Winner: {winning_candidate}
--------------------------
'''
    print( winning_candidate_results)
    txt_file.write(winning_candidate_results)