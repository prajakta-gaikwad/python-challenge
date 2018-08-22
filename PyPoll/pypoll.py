#Dependencies
import os
import csv

#path to the csv file
pyPoll_path = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join('..', 'Resources', 'pypollresults.csv')

#opening the csv file with built-in open function
#Using with ..as to lock the file resource    

with open (pyPoll_path, 'r') as csvfile:
    #Reading from the csv file
    csv_reader = csv.reader(csvfile, delimiter= ',')
    header = next(csv_reader)
    
    total_votes = 0
    candidates = []
    max_votes = 0
    winner = 0
    
    for i, row in enumerate(csv_reader):
        total_votes += 1
        candidate = row[2]
        candidates.append(candidate)
        
    from collections import Counter
    poll_data = Counter(candidates)      

with open (output_path, 'w') as csvw_file:
    #csvwriter = csv.writer(csvw_file)
    #csvwriter.writerow("Election Results")
    csvw_file.write("Election Results\n")
    csvw_file.write("----------------------------------------------\n")
    csvw_file.write(f'Total Votes: {total_votes}\n')
    csvw_file.write("----------------------------------------------\n")     
    print("")
    print("Election Results")
    print("----------------------------------------------")
    print(f'Total Votes: {total_votes}')
    print("----------------------------------------------")
    for key, value in poll_data.items():
        print(f'{key}: {round(((value/total_votes)*100),3)}% ({value})')
        csvw_file.write(f'{key}: {round(((value/total_votes)*100),3)}% ({value})\n')
        if value > max_votes:
            max_votes = value
            winner = key
    print("----------------------------------------------")  
    print(f'Winner: {winner}')
    print("----------------------------------------------")  
    csvw_file.write("----------------------------------------------\n")  
    csvw_file.write(f'Winner: {winner}\n')
    csvw_file.write("----------------------------------------------\n")  