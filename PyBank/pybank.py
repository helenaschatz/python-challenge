### PyBank Instructions

#In this challenge, you are tasked with creating a Python script to analyze the financial records of your company.
#You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
#The dataset is composed of two columns: "Date" and "Profit/Losses". 
#(Thankfully, your company has rather lax standards for accounting, so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#* The total number of months included in the dataset

#* The net total amount of "Profit/Losses" over the entire period

#* The changes in "Profit/Losses" over the entire period, and then the average of those changes

#* The greatest increase in profits (date and amount) over the entire period

#* The greatest decrease in profits (date and amount) over the entire period

#Your analysis should look similar to the following:

#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $22564198
#  Average Change: $-8311.11
#  Greatest Increase in Profits: Aug-16 ($1862002)
#  Greatest Decrease in Profits: Feb-14 ($-1825558)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os 
import csv


total_months = []
total_profit = []
monthly_profit_change = []


budgetdata=os.path.join('Resources','budget_data.csv') 

with open(budgetdata) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")


    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
budget_data=os.path.join( "Resources", "Financial_Analysis_Summary.txt")

with open(budget_data,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")














