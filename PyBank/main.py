# Modules
import os 
import csv 

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header 
    csv_header = next(csvreader)

    # Set variables 
    total_months = 0
    total_amount = 0
    previous = "x" 
    total_changes = 0 
    changes = 0 
    greatest_increase = 0 
    greatest_decrease = 0
    greatest_increase_date = 0  
    greatest_decrease_date = 0

    # Loop through csv
    for row in csvreader:
        
    # Calculate the total number of months
        total_months = total_months + 1
    
    # Calculate the total amount of "Profit/Losses"
        total_amount = total_amount + int(row[1])
        
    # Calculate the total of the changes in "Profit/Losses"
        current = int(row[1])

        if previous != "x":
            changes = current - previous
            total_changes = total_changes + changes

        previous = current

    # Calculate the greatest increase in profits (date and amount) 
        if changes > greatest_increase:
            greatest_increase = changes
            greatest_increase_date = row[0] 

    # Calculate the greatest decrease in losses (date and amount) 
        if changes < greatest_decrease:
            greatest_decrease = changes
            greatest_decrease_date = row[0] 

    # Calculate the average of the changes in "Profit/Losses"
    average_change = total_changes/(total_months-1)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_amount))
print("Average Change: $" +str (round(average_change,2)))
print("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) +")")
print("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) +")")

# Specify the file to write to
analysis_path = os.path.join("analysis", "analysis.txt")

# Open the analysis file using "write" mode, and then write the analysis to the .txt
with open(analysis_path, 'w') as txtfile:
    txtfile.write ("Financial Analysis\n") 
    txtfile.write ("----------------------------\n")
    txtfile.write ("Total Months: " + str(total_months) + "\n")
    txtfile.write ("Total: $" + str(total_amount) + "\n")
    txtfile.write ("Average Change: $" + str (round(average_change,2))  + "\n")    
    txtfile.write ("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) +")"  + "\n")
    txtfile.write ("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) +")"  + "\n")

