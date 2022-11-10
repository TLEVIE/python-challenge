import csv
import os

budgetdata = os.path.join("Resources", "budget_data.csv")

dates = []
netchange = []

currentvalue = 0
nettotal = 0
previousnumber = 0
difference = 0

# Open and read csv
with open(budgetdata) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

        currentvalue = int(row[1])

        # adding each date to a list
        dates.append(row[0])

        # calculating the profit/loss value
        nettotal = nettotal + currentvalue

        # skips the first entry
        if previousnumber != 0:
    
            difference = currentvalue - previousnumber
            netchange.append(difference)

        previousnumber = currentvalue

# find index of max/min values to match up with date list when printing
max_value = max(netchange)
max_index = netchange.index(max_value)
min_value = min(netchange)
min_index = netchange.index(min_value)

# calculate avg of the change amounts
avg = sum(netchange) / len(netchange)

# print results to terminal
print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(len(dates)))
print("Total: $" + str(nettotal))
print("Average Change: $" + str(round(avg, 2)))
print("Greatest Increase in Profits: " + str(dates[max_index+1]) + " ($" + str(max(netchange)) +")")
print("Greatest Decrease in Profits: " + str(dates[min_index+1]) + " ($" + str(min(netchange)) +")")

# print results to financialanalysis.txt
lines = ["Financial Analysis", 
"--------------------",
"Total Months: " + str(len(dates)), 
"Total: $" + str(nettotal), 
"Average Change: $" + str(round(avg, 2)), 
"Greatest Increase in Profits: " + str(dates[max_index+1]) + " ($" + str(max(netchange)) +")", 
"Greatest Decrease in Profits: " + str(dates[min_index+1]) + " ($" + str(min(netchange)) +")" ]

with open('financialanalysis.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')