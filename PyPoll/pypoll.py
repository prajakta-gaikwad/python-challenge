"""
Analyzing votes

"""
#import Dependencies
import os
import csv

#path to the csv file
pyPoll_path = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join('..', 'Resources', 'pypollresults.txt')

#opening the csv file with built-in open function
#Using with ..as to lock the file resource    

with open (pyPoll_path, 'r') as csvfile:
    #Reading from the csv file
    csv_reader = csv.reader(csvfile, delimiter= ',')
    header = next(csv_reader)
    
    #setting the variables
    total_votes = 0
    candidates = []
    max_votes = 0
    winner = 0
    
    for i, row in enumerate(csv_reader):
        #calculating total number of votes cast
        total_votes += 1
        #creating a list of all candidates including duplicates
        candidate = row[2]
        candidates.append(candidate)
    
    #Getting unique values and their count from a list    
    from collections import Counter
    poll_data = Counter(candidates)      

#Exporting a text file with the results and printing the analysis to the terminal
with open (output_path, 'w') as txtw_file:
    #csvwriter = csv.writer(csvw_file)
    #csvwriter.writerow("Election Results")
    txtw_file.write("Election Results\n")
    txtw_file.write("----------------------------------------------\n")
    txtw_file.write(f'Total Votes: {total_votes}\n')
    txtw_file.write("----------------------------------------------\n")     
    print("")
    print("Election Results")
    print("----------------------------------------------")
    print(f'Total Votes: {total_votes}')
    print("----------------------------------------------")
    
    #outcome of counter function is a dictionary
    #formatting the outcome in desired format
    #calculating percentages 
    for key, value in poll_data.items():
        print(f'{key}: {round(((value/total_votes)*100),3)}% ({value})')
        txtw_file.write(f'{key}: {round(((value/total_votes)*100),3)}% ({value})\n')
        #finding the winner based on popular vote
        if value > max_votes:
            max_votes = value
            winner = key
    print("----------------------------------------------")  
    print(f'Winner: {winner}')
    print("----------------------------------------------")  
    txtw_file.write("----------------------------------------------\n")  
    txtw_file.write(f'Winner: {winner}\n')
    txtw_file.write("----------------------------------------------\n")  