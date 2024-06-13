import os   
import csv

# Absolute path to the CSV file
election_data_csv = 'C:\\Users\\user\\OneDrive\\Desktop\\Monash Notes\\Assgnment 3 Python\\Starter_Code\\PyPoll\\Resources\\election_data.csv'

# Check if the file exists at the specified path
if not os.path.exists(election_data_csv):
    print(f"File not found: {election_data_csv}")
else:
    # Print the title and separator
    print("Election Results")
    print("------------------")
    
    # Open the CSV file
    with open(election_data_csv, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        
        # Skip the header row
        next(csv_reader)
        
        # Initialize variables
        total_votes = 0
        candidate_votes = {}
        winner = ""
        winner_votes = 0
        
        # Loop through each row in the CSV file
        for row in csv_reader:
            # Increment the total number of votes
            total_votes += 1
            
            # Get the candidate name
            candidate = row[2]
            
            # Increment the candidate's vote count
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
        
        # Print the total number of votes
        print(f"Total Votes: {total_votes}")
        print("------------------")
        
        # Calculate and print the percentage of votes each candidate received
        for candidate, votes in candidate_votes.items():
            percentage = (votes / total_votes) * 100
            print(f"{candidate}: {percentage:.3f}% ({votes})")
            
            # Determine the winner
            if votes > winner_votes:
                winner_votes = votes
                winner = candidate
        
        # Print the winner
        print("------------------")
        print(f"Winner: {winner}")
        print("------------------")
