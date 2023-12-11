import os
import csv

# Set path for file
budget_data_csv = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("Analysis", "results.txt")

#declare variables
months= []
profit_changes =[]
Total_Months = 0
Total = 0
previous = 0
current = 0
change=0
greatest_increase = 0
greatest_decrease =0
greatest_increase_month_index =""
greatest_decrease_month_index =""

with open(budget_data_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header=next(csvreader)
    first_line=next(csvreader)
    Total_Months += 1
    previous=float(first_line[1])
    Total+=previous
    
# Total months

    # add up the months and total profits/losses
    for row in csvreader:
        Total_Months += 1
       
        #total profits
        Total+=float(row[1])
        change=float(row[1]) - previous
        previous=float(row[1])
        profit_changes.append(change)

        #percentages between months
        if change > greatest_increase:
            greatest_increase=change
            greatest_increase_month_index=row[0]
        #find the greatest increase and decrease
        if change < greatest_decrease:
            greatest_decrease=change
            greatest_decrease_month_index=row[0]
#average the losses and profits
average=round(sum(profit_changes)/len(profit_changes), 2)

#create results variable for printing
results = f'''
Financial Analysis
----------------------------
Total Months: {Total_Months}
Total: ${Total}
Average Change: ${average}
Greatest Increase in Profits: {greatest_increase_month_index} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month_index} (${greatest_decrease})
'''
#Print the results
print(results)

#output the text file
with open(output_file, "w") as outfile:
    outfile.write(results)

  