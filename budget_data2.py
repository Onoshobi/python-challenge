import os
import csv

# Absolute path to the CSV file
budget_data2_csv = 'C:\\Users\\user\\OneDrive\\Desktop\\Monash Notes\\Assgnment 3 Python\\Starter_Code\\PyBank\\Resources\\budget_data2.csv'

# Check if the file exists at the specified path
if not os.path.exists(budget_data2_csv):
    print(f"File not found: {budget_data2_csv}")
else:
    try:
         # Print the title and separator
        print("Financial Analysis")
        print("------------------")

        # Open the CSV file
        with open(budget_data2_csv, newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            
            # Skip the header row
            next(csv_reader)
            
            # Track months and detect duplicates
            months = []
            duplicate_months = set()
            Profit = 0  # Initialize total sum
            previous_value = None  # Initialize previous value
            changes = []  # Initialize change list
            max_change = float('-inf')  # Initialize max profit change to negative infinity
            max_change_month = ""  # Initialize max change month
            min_change = float('inf')  # Initialize min profit change to positive infinity
            min_change_month = ""  # Initialize min change month
            
            for row in csv_reader:
                month = row[0]
                try:
                    value = int(row[1])  # Convert the second column to integer
                    Profit += value  # Sum the values in the second column

                    if previous_value is not None:
                        change = value - previous_value
                        changes.append(change)
                        
                        # Check for max change
                        if change > max_change:
                            max_change = change
                            max_change_month = month
                        
                        # Check for min change
                        if change < min_change:
                            min_change = change
                            min_change_month = month
                    
                    previous_value = value  # Update the previous value for the next iteration
            
                except ValueError:
                    print(f"Skipping non-integer value: {row[1]}")
                
                if month in months:
                    duplicate_months.add(month)
                else:
                    months.append(month)

            # Print the total number of months
            total_months = len(months)
            print(f"Total Months: {total_months}")
            
            # Print the total sum of the second column
            print(f"Total: ${Profit}")
            
            # Check for duplicates and print the count if any
            if duplicate_months:
                print(f"Number of duplicate months found: {len(duplicate_months)}")

            # Calculate the average change
            if changes:
                average_change = sum(changes) / len(changes)
                print(f"Average Change: ${average_change:.2f}")
            else:
                print("No changes to calculate average.")
                
            # Print the month with the greatest profit change
            if max_change_month:
                print(f"Greatest Increase in Profits: {max_change_month} (${max_change})")
                
            # Print the month with the greatest decrease in profit change
            if min_change_month:
                print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})")
                
    except Exception as e:
        print(f"An error occurred: {e}")
